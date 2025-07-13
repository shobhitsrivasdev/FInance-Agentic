import yfinance as yf
from mcp.server.fastmcp import FastMCP
import requests

# Create the MCP server instance
mcp = FastMCP("Financial Data Server")

# The tool to fetch financial data from Yahoo
@mcp.tool()
def get_yahoo_data(stock_data: str) -> str:
    print(f"[debug-server] get_yahoo_data({stock_data})")

    stock = yf.Ticker(stock_data)
    financial_data = stock.history(period="5d") 
    
    return financial_data.to_string()

# The tool to fetch financial data from Reddit
@mcp.tool()
def get_reddit_data(stock_data: str) -> str:
    print(f"[debug-server] get_reddit_data({stock_data})")

    endpoint = f"https://www.reddit.com/r/all/search.json?q={stock_data}&restrict_sr=on&sort=relevance&t=all"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch Reddit data."

if __name__ == "__main__":
    # Start the server with SSE transport
    mcp.run(transport="sse")
