import streamlit as st
import requests
import os
import json
from datetime import datetime
import socket
from urllib.parse import urlparse

# Configuration variables
API_BASE_URL = os.getenv("ADK_API_URL", "http://localhost:8000")
APP_NAME = "manager_agent"
USER_ID = "user"

# 1. Create a session if not already in session_state
# if "session_id" not in st.session_state:
#     create_session_url = f"{API_BASE_URL}/apps/{APP_NAME}/users/{USER_ID}/sessions"
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(create_session_url, headers=headers)
#     if response.status_code == 200:
#         session_data = response.json()
#         st.write("Session creation response:", session_data)  # Debug print
#         st.session_state.session_id = session_data["session_id"]  # You may need to change this key after seeing the output
#     else:
#         st.error(f"Failed to create session: {response.text}")
#         st.stop()

# SESSION_ID = st.session_state.session_id
API_URL = "http://localhost:8000/dev-ui?app=manager_agent"
ROBOT_IMG = "https://cdn-icons-png.flaticon.com/512/4712/4712035.png"
PLANE_IMG = "https://em-content.zobj.net/source/microsoft-teams/337/airplane_2708-fe0f.png"

# Configuration variables - separate UI and API URLs
UI_BASE_URL = os.getenv("ADK_UI_URL", "http://localhost:8000/dev-ui")
API_KEY = os.getenv("GOOGLE_API_KEY", "IzaSyBPTGOdGcqHd_8suR_wV4JSuT7DRhCfQoQy")

def check_server_status(url):
    """Check if the server is running and accessible."""
    try:
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        port = parsed_url.port or (443 if parsed_url.scheme == 'https' else 80)
        
        # Try to establish a connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        
        return result == 0
    except Exception:
        return False

def test_api_connection():
    """Test the API connection and return status."""
    try:
        # Test the base URL first
        response = requests.get(API_BASE_URL, timeout=5)
        if response.status_code == 200:
            # Then test the chat endpoint
            response = requests.get(API_URL, timeout=5)
            return response.status_code in [200, 405]  # 405 is okay as it means the endpoint exists
        return False
    except requests.exceptions.RequestException:
        return False

# Page configuration
st.set_page_config(
    page_title="Travel Insurance AI",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Check server status
server_status = check_server_status(API_BASE_URL)
api_status = test_api_connection()

# Custom CSS for advanced look
st.markdown(f"""
    <style>
    body, .stApp {{
        background: linear-gradient(135deg, #232526 0%, #414345 100%) !important;
        color: #f5f6fa;
    }}
    .main {{ padding: 2rem; }}
    .stChatMessage {{
        padding: 1.2rem;
        border-radius: 1.2rem;
        margin-bottom: 1.2rem;
        background: linear-gradient(120deg, #232526 60%, #3a3a3a 100%);
        box-shadow: 0 2px 12px 0 rgba(0,0,0,0.10);
    }}
    .quick-action-btn {{
        background: linear-gradient(90deg, #6dd5ed 0%, #2193b0 100%);
        color: white !important;
        border: none;
        border-radius: 2em;
        padding: 0.7em 1.5em;
        font-size: 1.1em;
        margin: 0.3em 0.5em 0.3em 0;
        box-shadow: 0 2px 8px 0 rgba(33,147,176,0.10);
        transition: background 0.2s, box-shadow 0.2s;
        cursor: pointer;
    }}
    .quick-action-btn:hover {{
        background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 100%);
        box-shadow: 0 4px 16px 0 rgba(33,147,176,0.18);
    }}
    .section-header {{
        font-size: 1.5em;
        font-weight: 700;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
        color: #6dd5ed;
        display: flex;
        align-items: center;
        gap: 0.5em;
    }}
    .example-query {{
        color: #b0e0ef;
        font-style: italic;
        margin: 0.5rem 0;
        font-size: 1.1em;
    }}
    .stTextInput>div>div>input {{
        background: #232526;
        color: #f5f6fa;
        border-radius: 1em;
        border: 1px solid #6dd5ed;
    }}
    .stButton>button {{
        background: linear-gradient(90deg, #6dd5ed 0%, #2193b0 100%);
        color: white;
        border-radius: 2em;
        font-size: 1.1em;
        margin: 0.3em 0.5em 0.3em 0;
        border: none;
        box-shadow: 0 2px 8px 0 rgba(33,147,176,0.10);
        transition: background 0.2s, box-shadow 0.2s;
    }}
    .stButton>button:hover {{
        background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 100%);
        box-shadow: 0 4px 16px 0 rgba(33,147,176,0.18);
    }}
    </style>
""", unsafe_allow_html=True)

# Centered, gradient header with icons
st.markdown(
    f"""
    <div style='width:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:1.5em;'>
        <div style='display:flex;align-items:center;gap:1em;background:linear-gradient(90deg,#6dd5ed 0%,#2193b0 100%);padding:1em 2em;border-radius:2em;box-shadow:0 2px 16px 0 rgba(33,147,176,0.10);'>
            <img src='{ROBOT_IMG}' width='60'/>
            <h1 style='display:inline;margin:0;font-size:2.5em;color:#fff;text-shadow:1px 2px 8px #2193b0;'>Travel Insurance AI Assistant</h1>
            <img src='{PLANE_IMG}' width='48'/>
        </div>
        <div style='margin-top:0.7em;color:#b0e0ef;font-size:1.1em;text-align:center;'>
            🤖 This application provides access to various insurance-related agents, all coordinated by the Manager Agent.<br>
            Type your question below or use the quick actions to get started!
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_start_time" not in st.session_state:
    st.session_state.chat_start_time = datetime.now()

col1, _, col3 = st.columns([3, 1, 1])

with col1:
    st.markdown("<div class='section-header'>🚀 Quick Actions</div>", unsafe_allow_html=True)
    quick_actions = [
        ("Check Eligibility", "I want to check if I'm eligible for travel insurance", "📝"),
        ("View Plans", "What travel insurance plans do you offer?", "📄"),
        ("File Claim", "I need to file a claim for my travel insurance", "📑"),
        ("Check Status", "What's the status of my claim?", "🔎"),
        ("Get Quote", "Can I get a quote for travel insurance?", "💸"),
        ("Cancel Policy", "I want to cancel my travel insurance policy", "❌")
    ]
    cols = st.columns(3)
    for idx, (action, query, icon) in enumerate(quick_actions):
        with cols[idx % 3]:
            if st.button(f"{icon} {action}", key=f"action_{idx}", help=query):
                st.session_state.messages.append({"role": "user", "content": query})
                st.rerun()
    st.markdown("<div class='section-header'>💬 Chat</div>", unsafe_allow_html=True)
    st.markdown("Try asking about:")
    example_queries = [
        "What's covered in the basic travel insurance plan?",
        "How do I file a claim for lost luggage?",
        "What's the process for getting a refund?",
        "Can I get insurance for my international trip?"
    ]
    for query in example_queries:
        st.markdown(f'<div class="example-query">💡 {query}</div>', unsafe_allow_html=True)
    # Display chat history with avatars
    for message in st.session_state.messages:
        avatar = None
        if message["role"] == "assistant":
            avatar = ROBOT_IMG
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
    # Chat input and response
    prompt = st.chat_input("Ask me anything about travel insurance...")
    if prompt is not None:
        prompt = prompt.strip()
        if not prompt:
            st.warning("Please enter a message.")
        else:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant", avatar=ROBOT_IMG):
                with st.spinner("Thinking..."):
                    try:
                        headers = {
                            "Content-Type": "application/json",
                            "Accept": "application/json"
                        }
                        payload = {
                            "message": prompt
                        }
                        st.session_state.last_request = {
                            "url": API_URL,
                            "payload": payload,
                            "headers": headers,
                            "timestamp": datetime.now().isoformat()
                        }
                        response = requests.post(
                            API_URL,
                            json=payload,
                            headers=headers,
                            timeout=60
                        )
                        if response.status_code == 200:
                            data = response.json()
                            answer = data.get("output", data.get("response", "No response from agent."))
                        else:
                            answer = f"Error from ADK server: {response.status_code} - {response.text}"
                            st.error(f"Error details: URL={API_URL}, Status={response.status_code}")
                        st.markdown(answer)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
                        st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}"})

with col3:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat_start_time = datetime.now()
        st.rerun()
    st.divider()
    if st.checkbox("Show Debug Information"):
        st.markdown("### 🔧 Debug Info")
        st.code(f"UI Base URL: {UI_BASE_URL}\nAPI Base URL: {API_BASE_URL}\nAPI Endpoint: {API_URL}")
        if "last_request" in st.session_state:
            st.json(st.session_state.last_request)

st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Travel Insurance AI Assistant | Powered by Google ADK</p>
    </div>
""", unsafe_allow_html=True)