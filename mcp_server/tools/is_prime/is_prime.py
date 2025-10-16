"""This is an MCP tool that checks if a number is prime."""
from server import mcp


@mcp.tool()
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
