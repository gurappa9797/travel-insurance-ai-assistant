from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .sub_agents import (
    refund_agent, payment_agent, vetting_agent, coverage_agent, flight_agent,
    explore_plans_agent, purchase_plan_agent, claim_agent, cancel_agent
)

root_agent = Agent(
    name="manager_agent",
    model="gemini-2.5-pro-preview-03-25",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.
    Always delegate the task to the appropriate agent. Use your best judgement to determine which agent to delegate to.
    You are responsible for delegating tasks to the following agents:
    - vetting_agent
    - coverage_agent
    - payment_agent
    - refund_agent
    - flight_agent
    - explore_plans_agent
    - purchase_plan_agent
    - claim_agent
    - cancel_agent
    """,
    sub_agents=[
        vetting_agent, coverage_agent, payment_agent, refund_agent, flight_agent,
        explore_plans_agent, purchase_plan_agent, claim_agent, cancel_agent
    ],
)

# Expose root_agent as agent attribute for ADK framework
agent = root_agent

# Expose sub-agents for direct use
__all__ = [
    "root_agent", "vetting_agent", "coverage_agent", "payment_agent", "refund_agent", "flight_agent",
    "explore_plans_agent", "purchase_plan_agent", "claim_agent", "cancel_agent"
] 