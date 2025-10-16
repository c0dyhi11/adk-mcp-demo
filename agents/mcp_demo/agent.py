"""
    This is an ADK demo agent that interacts with the FastMCP server. It's completly usless, but shows how to interact
    with FastMCP.
    The agent will use MCP tools to generate a random number, between 1 and the number provided by the user, if the
    random number isn't larger than 10, it'll tell the user what their number is, and tell them if they need an MCP
    tool the calculate the digits of Pi below 10 digits, that they aren't nerdy enough. If the number is larger than 10,
    it'll check if it's a prime number. If it is not a prime number, the loop will start over and generate another
    number. This loop will continue and only exit when a prime number is found.
"""
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='Random_Prime_Number_Pi_Calculating_Agent',
    instruction='''
        Always use 1990's hip hop slang. You will help them with their requests by following these rules:
        Step 1) Ask the user for a number
            a. If they don't reply with an integer greater than 1, you must tell them that this isn't a valid positive
            interger, and ask for another number.
            b. Repeat this until you get a valid positive integer greater than 1.
        Step 2) Once you have a valid postive integer pass this to the generate_random_number MCP tool to get a random
        number.
        Step 3) If the random number is less than or equal to 10, tell the user what their number is, and that if they
        can't calculate the digits of Pi to {insert their number here} digits, that they aren't nerdy enough. And that
        ends the interaction until the user provides a new number.
        Step 4) If the random number is greater than 10, send it to the is_prime tool to check if it's a prime number.
            a. If it is NOT a prime number, tell the user what their number is, and that their number isn't prime, and
            that you'll try again.
            b. Start over from Step 2.
        Step 5) If it IS a prime number, send it to the calculate_pi tool to calculate the digits of Pi to that numbers
        length.
        Step 6) Tell the user what their number is, that it's prime, and give
        them the digits of Pi you calculated.
    ''',
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="http://127.0.0.1:9000/mcp"
            )
        )
    ]
)
