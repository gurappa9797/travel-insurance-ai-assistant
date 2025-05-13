import streamlit as st
import requests

API_KEY = "AIzaSyBPTGOdGcqHd_8suR_wV4JSuT7DRhCfQoQ"
# GOOGLE_PROJECT_ID=t360-458812"  # <-- Replace with your real API key

# Set page config
st.set_page_config(
    page_title="Insurance ADK Agents",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title and description
st.title("🤖 Insurance ADK Agents")
st.markdown("""
This application provides access to various insurance-related agents, all coordinated by the Manager Agent:
- Vetting Agent: Handles insurance eligibility checks
- Coverage Agent: Manages insurance coverage details
- Payment Agent: Handles payment processing
- Refund Agent: Manages refund requests

**Type your question below. The Manager Agent will automatically delegate to the right specialist!**
""")

# Sidebar for agent selection
st.sidebar.title("About")
st.sidebar.info("""
You are chatting with the Manager Agent. It will route your request to the appropriate sub-agent (Vetting, Coverage, Payment, Refund) as needed.
""")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                url = "http://localhost:8000/api/chat/manager_agent"
                payload = {"message": prompt}
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                }
                response = requests.post(url, json=payload, headers=headers, timeout=60)
                if response.status_code == 200:
                    answer = response.json().get("response", "No response from agent.")
                else:
                    answer = f"Error from ADK server: {response.text}"
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}"})

# Add a clear chat button in the sidebar
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# print(dir(root_agent)) 