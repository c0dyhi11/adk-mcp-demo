"""This is an MCP tool that generates a random number."""
import random
from server import mcp


@mcp.tool()
def generate_random_number(max_number: int = 100) -> int:
    """
    Returns a random number between 1 and max_number.
    """
    return random.randint(1, max_number)
