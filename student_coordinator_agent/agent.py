import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from student_coordinator_agent.prompt import STUDENT_COORDINATOR_INSTRUCTION
from dotenv import load_dotenv

load_dotenv(override=True)

root_agent = Agent(
    name="student_coordinator_agent",
    model="gemini-2.0-flash",
    description="An agent that assists students with their inquiries and provides relevant information.",
    instruction=STUDENT_COORDINATOR_INSTRUCTION,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=os.getenv("FIA_MCP_URL", "https://fia-axcelerate-mcp-905053609184.us-central1.run.app/mcp"),
                timeout=30
            )
        )
    ]
)