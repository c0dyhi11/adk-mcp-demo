"""Entry point for running the MCP server."""
from server import mcp
import tools  # All tools in this directory will be auto-discovered and registered.


def main():
    """Entry point for running the MCP server."""
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=9000,
        log_level="DEBUG",
    )


if __name__ == "__main__":
    main()
