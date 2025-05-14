import streamlit as st

st.set_page_config(page_title="Travel Insurance", page_icon=":blue_book:", layout="centered")

def show_navbar():
    st.markdown(
        """
        <div style="background-color:#1976d2;padding:20px 0 10px 0;margin:-3em -3em 2em -3em;">
            <h2 style="color:white;text-align:center;margin:0;">Travel Insurance</h2>
            <div style="float:right;margin-top:-2.5em;">
                <a href="?page=dashboard" style="color:white;margin-right:20px;text-decoration:none;">Dashboard</a>
                <a href="?page=verify" style="color:white;margin-right:20px;text-decoration:none;">Verify Ticket</a>
                <a href="?page=plans" style="color:white;margin-right:20px;text-decoration:none;">Insurance Plans</a>
                <a href="?page=refund" style="color:white;margin-right:20px;text-decoration:none;">Refund Status</a>
                <a href="?page=logout" style="color:white;text-decoration:none;">Logout</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def show_dashboard(user_name="User"):
    show_navbar()
    st.success("Logged in successfully!")
    st.markdown(
        f"""
        <div style="display:flex;justify-content:center;align-items:center;">
            <div style="width:70%;margin-top:2em;">
                <h2 style="text-align:center;">Welcome, {user_name}!</h2>
                <div style="display:flex;justify-content:center;gap:2em;margin-top:2em;">
                    <div style="border:1px solid #eee;padding:2em 2em 1.5em 2em;border-radius:10px;text-align:center;width:250px;">
                        <h4>Verify Ticket</h4>
                        <p>Check your ticket status and eligibility</p>
                        <a href="?page=verify"><button style="background:#1976d2;color:white;border:none;padding:8px 24px;border-radius:5px;">Verify Now</button></a>
                    </div>
                    <div style="border:1px solid #eee;padding:2em 2em 1.5em 2em;border-radius:10px;text-align:center;width:250px;">
                        <h4>Insurance Plans</h4>
                        <p>Browse available insurance plans</p>
                        <a href="?page=plans"><button style="background:#1976d2;color:white;border:none;padding:8px 24px;border-radius:5px;">View Plans</button></a>
                    </div>
                    <div style="border:1px solid #eee;padding:2em 2em 1.5em 2em;border-radius:10px;text-align:center;width:250px;">
                        <h4>Refund Status</h4>
                        <p>Check your refund status</p>
                        <a href="?page=refund"><button style="background:#1976d2;color:white;border:none;padding:8px 24px;border-radius:5px;">Check Status</button></a>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def show_register():
    st.markdown(
        """
        <div style="background-color:#1976d2;padding:20px 0 10px 0;margin:-3em -3em 2em -3em;">
            <h2 style="color:white;text-align:center;margin:0;">Travel Insurance</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h3 style='text-align:center;'>Register</h3>", unsafe_allow_html=True)
    with st.form("register_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email address")
        password = st.text_input("Password", type="password")
        register_btn = st.form_submit_button("Register")
        if register_btn:
            st.success("Registration successful! Please log in.")
            st.session_state["registered_name"] = full_name
            st.session_state["page"] = "login"
            st.rerun()

    st.markdown(
        """
        <div style="text-align:center;margin-top:1em;">
            Already have an account? <a href="?page=login">Login here</a>
        </div>
        <hr>
        <div style="text-align:center;">
            <button style="background:white;border:1px solid #ccc;padding:8px 16px;border-radius:4px;display:flex;align-items:center;justify-content:center;margin:auto;">
                <img src="https://developers.google.com/identity/images/g-logo.png" width="20" style="margin-right:8px;">
                Sign up with Google
            </button>
        </div>
        """,
        unsafe_allow_html=True,
    )

def show_login():
    st.markdown(
        """
        <div style="background-color:#1976d2;padding:20px 0 10px 0;margin:-3em -3em 2em -3em;">
            <h2 style="color:white;text-align:center;margin:0;">Travel Insurance</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h3 style='text-align:center;'>Login</h3>", unsafe_allow_html=True)
    with st.form("login_form"):
        email = st.text_input("Email address")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")
        if login_btn:
            st.success("Login successful! Welcome back.")
            st.session_state["logged_in"] = True
            st.session_state["user_name"] = st.session_state.get("registered_name", "User")
            st.session_state["page"] = "dashboard"
            st.rerun()

    st.markdown(
        """
        <div style="text-align:center;margin-top:1em;">
            Don't have an account? <a href="?page=register">Register here</a>
        </div>
        <hr>
        <div style="text-align:center;">
            <button style="background:white;border:1px solid #ccc;padding:8px 16px;border-radius:4px;display:flex;align-items:center;justify-content:center;margin:auto;">
                <img src="https://developers.google.com/identity/images/g-logo.png" width="20" style="margin-right:8px;">
                Sign in with Google
            </button>
        </div>
        """,
        unsafe_allow_html=True,
    )

def show_verify_ticket():
    show_navbar()
    st.markdown("<h2 style='text-align:center;'>Verify Ticket</h2>", unsafe_allow_html=True)
    st.info("This is a placeholder for the Verify Ticket page. Add your ticket verification logic here.")

def show_insurance_plans():
    show_navbar()
    st.markdown("<h2 style='text-align:center;'>Insurance Plans</h2>", unsafe_allow_html=True)
    st.info("This is a placeholder for the Insurance Plans page. Add your plans listing and details here.")

def show_refund_status():
    show_navbar()
    st.markdown(
        """
        <h2 style='margin-top:1em;'>Request Refund</h2>
        <p>Enter your transaction ID to request a refund for your insurance plan.</p>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        with st.form("refund_form", border=False):
            st.markdown(
                """
                <style>
                .stTextInput>div>div>input {border-radius: 4px 0 0 4px;}
                .scan-btn {border-radius: 0 4px 4px 0; margin-left:-4px;}
                </style>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("**Transaction ID**")
            tcol1, tcol2 = st.columns([5,1])
            transaction_id = tcol1.text_input("Enter your transaction ID from payment confirmation", key="refund_tid", label_visibility="collapsed", help="You can find this in your payment confirmation email or on the payment confirmation page.")
            scan = tcol2.button("Scan", key="scan_btn")
            st.caption("You can find this in your payment confirmation email or on the payment confirmation page.")

            reason = st.selectbox("Reason for Refund", [
                "Select a reason",
                "Trip cancelled",
                "Duplicate payment",
                "Service issue",
                "Medical emergency",
                "Other"
            ])
            submit, cancel = st.columns([2,1])
            submit_btn = submit.form_submit_button("Submit Refund Request", use_container_width=True)
            cancel_btn = cancel.form_submit_button("Cancel", use_container_width=True)
            if submit_btn:
                st.success("Refund request submitted!")
            elif cancel_btn:
                st.info("Refund request cancelled.")

    with col2:
        st.markdown(
            """
            <div style="border:1px solid #eee;padding:1.5em 1em 1em 1em;border-radius:10px;margin-bottom:1.5em;">
                <b>Refund Assistant</b>
                <ul style="margin-top:0.5em;">
                    <li>Finding your transaction ID</li>
                    <li>Understanding refund eligibility</li>
                    <li>Checking refund status</li>
                    <li>Explaining refund process</li>
                </ul>
                <button style="background:#fff;border:1px solid #1976d2;color:#1976d2;padding:6px 18px;border-radius:5px;margin-top:0.5em;">Get General Assistance</button>
            </div>
            <div style="border:1px solid #eee;padding:1em;border-radius:10px;">
                <b>Recent Refunds</b>
                <div style="color:#d32f2f;margin-top:0.5em;">Error loading recent refunds</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Routing logic
query_page = st.query_params.get("page")
if "page" in st.session_state:
    page = st.session_state["page"]
elif query_page:
    page = query_page
else:
    page = "register"

if page == "login":
    show_login()
elif page == "dashboard":
    show_dashboard(st.session_state.get("user_name", "User"))
elif page == "register":
    show_register()
elif page == "logout":
    st.session_state.clear()
    st.success("Logged out!")
    show_login()
elif page == "verify":
    show_verify_ticket()
elif page == "plans":
    show_insurance_plans()
elif page == "refund":
    show_refund_status()
else:
    show_register()
