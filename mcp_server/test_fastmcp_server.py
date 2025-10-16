"""This is a simple test script to verify that the FastMCP server is running correctly and tools are detected."""
import asyncio
from fastmcp import Client


client = Client("http://127.0.0.1:9000/mcp")


async def main():
    """Main function to test the FastMCP server."""
    async with client:
        await client.ping()
        tools = await client.list_tools()
        print(tools)
asyncio.run(main())
