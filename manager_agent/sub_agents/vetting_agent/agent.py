from google.adk.agents import Agent


# ===1. User Vetting Agent === (handles user registration and MAC address verification) 
vetting_agent = Agent(
    name="vetting_agent",
    # model="gemini-2.5-pro-exp-03-25",
    model="gemini-2.5-pro-preview-03-25",
    description="Handles eligibility and vetting for travel insurance applicants.",
    instruction="""
You are a vetting agent. Your tasks include:
- Checking eligibility for travel insurance plans.
- Verifying user information and travel details.
- Ensuring compliance with policy requirements.
- Providing clear feedback on eligibility status.
""",
)