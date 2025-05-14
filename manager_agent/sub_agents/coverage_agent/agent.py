from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool  


# Coverage Agent
coverage_agent = Agent(
    name="coverage_agent",
    # model="gemini-2.5-pro-exp-03-25",
    model="gemini-2.5-pro-preview-03-25",
    description="Handles insurance coverage details and plan information.",
    instruction="""
You are a coverage agent. Your tasks include:
- Providing details about available insurance plans.
- Explaining coverage, exclusions, and benefits.
- Assisting users in selecting the right plan.
- Answering questions about policy terms and conditions.
""",
)