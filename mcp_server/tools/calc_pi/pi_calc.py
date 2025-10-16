"""This is an MCP tool that calculates Pi to a specified number of digits."""
import math
from server import mcp


@mcp.tool()
def calculate_pi_to_digits(digits: int) -> str:
    """
    Calculates Pi to a given number of digits.
    """
    return f"{math.pi:.{digits}f}"
