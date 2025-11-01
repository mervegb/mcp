from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

server_params = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"]
)

async def run():
    try:
        print("Starting stdio client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected, creating session...")
            async with ClientSession(read, write) as session:

                print("Initializing session...")
                await session.initialize()

                print("Listing tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)

                print("Calling tool...")
                result = await session.call_tool( "get_weather",{"location": "San Francisco"})
                print("Result:", result)
    except Exception as e:
        print("Exception:", e)
        traceback.print_exc()
    finally:
        print("Closing client...")


if __name__ == "__main__":
    asyncio.run(run())        