# search_agent.py
import asyncio
import os
import shutil
import subprocess
import time
from typing import Any

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings

# Initialize the search agent
search_agent = Agent(
    name="Assistant",
    instructions="Use the tools to answer the questions.",
    model_settings=ModelSettings(tool_choice="required"),
)

async def run(mcp_server: MCPServer):
    search_agent.mcp_servers = [mcp_server]  # Assign MCP server dynamically
    message = "Search on Yahoo Finance for financial data"
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=search_agent, input=message)
    # Save result to a text file
    with open("financial_report.txt", "w", encoding="utf-8") as f:
        f.write(str(result))  # Ensure result is stringified
    return result

async def main():
    async with MCPServerSse(
        name="SSE Python Server",
        params={"url": "http://localhost:8000/sse"},  # URL of the server
    ) as server:
        trace_id = gen_trace_id()
        with trace(workflow_name="SSE Example", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
            await run(server)

if __name__ == "__main__":
    if not shutil.which("uv"):
        raise RuntimeError(
            "uv is not installed. Please install it: https://docs.astral.sh/uv/getting-started/installation/"
        )

    # Running the SSE server in a subprocess (this is simulating a remote server)
    process: subprocess.Popen[Any] | None = None
    try:
        this_dir = os.path.dirname(os.path.abspath(__file__))
        server_file = os.path.join(this_dir, "search_agent_server.py")

        print("Starting SSE server at http://localhost:8000/sse ...")

        process = subprocess.Popen(["uv", "run", server_file])

        time.sleep(3)

        print("SSE server started. Running example...\n\n")
    except Exception as e:
        print(f"Error starting SSE server: {e}")
        exit(1)

    try:
        asyncio.run(main())
    finally:
        if process:
            process.terminate()
