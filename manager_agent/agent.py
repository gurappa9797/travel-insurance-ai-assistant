from google.adk.agents import Agent
from .sub_agents import refund_agent, payment_agent, vetting_agent, coverage_agent

root_agent = Agent(
    name="manager_agent",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.
    Always delegate the task to the appropriate agent. Use your best judgement to determine which agent to delegate to.
    You are responsible for delegating tasks to the following agent:
    - vetting_agent
    - coverage_agent
    - payment_agent
    - refund_agent
    """,
    sub_agents=[vetting_agent, coverage_agent, payment_agent, refund_agent],
)

# Expose root_agent as agent attribute for ADK framework
agent = root_agent

# Expose sub-agents for direct use
__all__ = ["root_agent", "vetting_agent", "coverage_agent", "payment_agent", "refund_agent"] 