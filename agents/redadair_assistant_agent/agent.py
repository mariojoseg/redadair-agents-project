import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from redadair_assistant_agent.prompt import REDADAIR_AGENT_INSTRUCTION
from dotenv import load_dotenv

load_dotenv(override=True)

root_agent = Agent(
    name="redadair_assistant_agent",
    model="gemini-2.0-flash",
    description="An agent that assists students with their inquiries and provides relevant information.",
    instruction=REDADAIR_AGENT_INSTRUCTION,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=os.getenv("REDADAIR_MCP_URL", "https://redadair-mcp-server-905053609184.us-central1.run.app/mcp"),
                timeout=30
            )
        )
    ]
)