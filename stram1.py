import streamlit as st
import requests
import os
import json
import traceback
import time

# Configuration variables
ADK_BASE_URL = os.getenv("ADK_URL", "http://localhost:8000")
API_KEY = os.getenv("GOOGLE_API_KEY", "IzaSyBPTGOdGcqHd_8suR_wV4JSuT7DRhCfQoQy")

# Let's fix the URL construction - important change here
# It looks like dev-ui might be a frontend, not part of the API path
DEFAULT_API_URL = f"{ADK_BASE_URL}/api/v1/chat"

st.set_page_config(page_title="Travel Insurance AI - Debug Mode", page_icon=":wrench:", layout="wide")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_url" not in st.session_state:
    st.session_state.api_url = DEFAULT_API_URL
if "api_method" not in st.session_state:
    st.session_state.api_method = "POST"
if "last_response" not in st.session_state:
    st.session_state.last_response = None
if "api_test_results" not in st.session_state:
    st.session_state.api_test_results = []

# Set up layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Travel Insurance AI Assistant - Debug Mode")
    st.markdown("Chat with our multi-agent system for travel insurance with enhanced debugging.")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Function to test endpoint with different methods and payloads
def test_endpoint(url, method, payload=None, params=None):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        start_time = time.time()
        
        if method == "GET":
            response = requests.get(url, params=params, headers=headers, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        elapsed = time.time() - start_time
        
        result = {
            "method": method,
            "url": url + (f"?{params}" if params and method == "GET" else ""),
            "status_code": response.status_code,
            "elapsed_time": f"{elapsed:.2f}s",
            "response_preview": str(response.text)[:100] + "..." if len(response.text) > 100 else response.text
        }
        
        return result
    except Exception as e:
        return {
            "method": method,
            "url": url,
            "status_code": "Error",
            "elapsed_time": "N/A",
            "response_preview": str(e),
            "error": traceback.format_exc()
        }

# Sidebar for settings and debugging
with col2:
    st.header("API Configuration")
    
    api_url = st.text_input("API Base URL", value=st.session_state.api_url)
    if api_url != st.session_state.api_url:
        st.session_state.api_url = api_url
    
    include_app_param = st.checkbox("Include 'app=manager_agent' parameter", value=True)
    app_param_location = st.radio("App parameter location", 
                                ["In query string", "In request body"], 
                                index=0)
    
    request_method = st.radio("Request Method", ["GET", "POST"], 
                             index=0 if st.session_state.api_method == "GET" else 1)
    st.session_state.api_method = request_method
    
    st.subheader("Request Payload")
    use_complex_payload = st.checkbox("Use complex message structure", value=False)
    
    # Session settings
    st.divider()
    st.subheader("Session Settings")
    session_id = st.text_input("Session ID", value="b85bdca1-4b35-46ed-a9ee-e69f05d1dede")
    user_id = st.text_input("User ID", value="user")
    
    # Test API connection
    st.divider()
    if st.button("Test API Connection"):
        with st.spinner("Testing API connections..."):
            results = []
            
            # Construct base URL
            base_url = st.session_state.api_url
            
            # Prepare parameters and payloads
            query_params = {"app": "manager_agent"} if include_app_param and app_param_location == "In query string" else None
            
            # Simple payload
            simple_payload = {
                "user_id": user_id,
                "session_id": session_id,
                "message": "test message"
            }
            
            # Complex payload
            complex_payload = {
                "app_name": "manager_agent" if include_app_param and app_param_location == "In request body" else None,
                "user_id": user_id,
                "session_id": session_id,
                "new_message": {
                    "parts": [{"text": "test message"}]
                }
            }
            
            # Remove None values
            complex_payload = {k: v for k, v in complex_payload.items() if v is not None}
            
            # Test GET with various combinations
            if include_app_param and app_param_location == "In query string":
                results.append(test_endpoint(base_url, "GET", params=query_params))
            else:
                results.append(test_endpoint(base_url, "GET"))
            
            # Test POST with various combinations
            active_payload = complex_payload if use_complex_payload else simple_payload
            
            if include_app_param and app_param_location == "In query string":
                full_url = f"{base_url}?app=manager_agent"
                results.append(test_endpoint(full_url, "POST", payload=active_payload))
            else:
                results.append(test_endpoint(base_url, "POST", payload=active_payload))
            
            st.session_state.api_test_results = results
    
    # Show test results
    if st.session_state.api_test_results:
        st.divider()
        st.subheader("API Test Results")
        for i, result in enumerate(st.session_state.api_test_results):
            with st.expander(f"Test {i+1}: {result['method']} - Status: {result['status_code']}"):
                st.write(f"**URL:** {result['url']}")
                st.write(f"**Response time:** {result['elapsed_time']}")
                st.write("**Response preview:**")
                st.code(result['response_preview'])
                if "error" in result:
                    st.error("Error details:")
                    st.code(result['error'])

# Chat input area (in main column)
with col1:
    if prompt := st.chat_input("Ask me anything about travel insurance..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    headers = {
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    }
                    
                    # Construct URL based on settings
                    request_url = st.session_state.api_url
                    if include_app_param and app_param_location == "In query string":
                        request_url = f"{request_url}?app=manager_agent"
                    
                    # Construct payload based on settings
                    if use_complex_payload:
                        payload = {
                            "user_id": user_id,
                            "session_id": session_id,
                            "new_message": {
                                "parts": [{"text": prompt}]
                            }
                        }
                        if include_app_param and app_param_location == "In request body":
                            payload["app_name"] = "manager_agent"
                    else:
                        payload = {
                            "user_id": user_id,
                            "session_id": session_id,
                            "message": prompt
                        }
                        if include_app_param and app_param_location == "In request body":
                            payload["app_name"] = "manager_agent"
                    
                    # Store request details for debugging
                    request_details = {
                        "url": request_url,
                        "method": st.session_state.api_method,
                        "payload": payload,
                        "headers": {k: v for k, v in headers.items() if k != "Authorization"}
                    }
                    st.session_state.last_request = request_details
                    
                    # Make the request based on the selected method
                    if st.session_state.api_method == "GET":
                        # For GET, convert payload to params
                        params = {k: json.dumps(v) if isinstance(v, (dict, list)) else v 
                                for k, v in payload.items()}
                        response = requests.get(
                            request_url.split('?')[0],  # Remove any query params in the URL 
                            params=params,
                            headers=headers, 
                            timeout=60
                        )
                    else:  # POST
                        response = requests.post(
                            request_url, 
                            json=payload, 
                            headers=headers, 
                            timeout=60
                        )
                    
                    # Store response for debugging
                    response_details = {
                        "status_code": response.status_code,
                        "headers": dict(response.headers),
                        "content": response.text[:1000] + ("..." if len(response.text) > 1000 else "")
                    }
                    st.session_state.last_response = response_details
                    
                    if response.status_code == 200:
                        try:
                            data = response.json()
                            if isinstance(data, list):
                                answer = data[0].get("output", data[0].get("response", "No response from agent."))
                            else:
                                answer = data.get("output", data.get("response", "No response from agent."))
                        except json.JSONDecodeError:
                            answer = "Received a non-JSON response from server:\n\n" + response.text[:500]
                    else:
                        answer = f"Error from ADK server: {response.status_code} - {response.text[:500]}"
                        
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.code(traceback.format_exc())
                    st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}"})

# Bottom controls
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()