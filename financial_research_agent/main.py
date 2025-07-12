# main.py
import asyncio
from .manager import FinancialResearchManager
from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings

import os
import shutil
import subprocess
import time
from typing import Any

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse

# Entrypoint for the financial bot example.
# Run this as `python -m examples.financial_bot.main` and enter a
# financial research query, for example:
# "Write up an analysis of Apple Inc.'s most recent quarter."
async def main() -> None:
    query = input("Enter a financial research query: ")

    mgr = FinancialResearchManager()

    # Ensure you pass the 'params' argument here
    mcp_server = MCPServerSse(
        name="SSE Python Server",  # Optional, for better logging
        params={
            "url": "http://localhost:8000/sse",  # Make sure this matches your server URL
        },
    )
    
    # Now pass the mcp_server instance to the run method
    await mgr.run(query, mcp_server)


if __name__ == "__main__":
    asyncio.run(main())

