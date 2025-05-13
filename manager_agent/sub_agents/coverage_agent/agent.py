from google.adk.agents import Agent


# Coverage Agent
coverage_agent = Agent(
    name="coverage_agent",
    model="gemini-2.5-pro-exp-03-25",
     description="Assesses and calculates Travel Insurance coverage options.",
    instruction="""Given Travel trip details and user requirements, calculate appropriate Travel coverage options
                   and premiums. Consider duration, risk factors, and coverage types.
                   
                   Provide 3 coverage levels: 
                   - Basic (50% coverage with 1% of ticket price as fee)
                   - Standard (75% coverage with 2% of ticket price as fee)
                   - Premium (100% coverage with 3% of ticket price as fee)
                   
                   Include details on coverage limits, exclusions, and premiums.
                   Ensure compliance with insurance regulations and guidelines."""   
           
)