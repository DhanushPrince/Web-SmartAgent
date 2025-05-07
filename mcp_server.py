import os
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from dotenv import load_dotenv
import asyncio

load_dotenv()

mcp_fetch_server = MCPServerStdio(
    command="python",
    args=["-m","mcp_server_fetch"]
)
os.environ["GROQ_API_KEY"]

agent = Agent(
    model = "groq:llama-3.3-70b-versatile",
    mcp_servers=[mcp_fetch_server]
)

#main async function
async def main():
    async with agent.run_mcp_servers():
        user = input("Enter url:")
        result = await agent.run(f"extract and summarize content:{user}")
        output = result.output 
        return output
    
if __name__=="__main__":
    output = asyncio.run(main())
    print(output)