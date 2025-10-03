import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from fia_assistant_agent.prompt import FIA_ASSISTANT_INSTRUCTION
from dotenv import load_dotenv

load_dotenv(override=True)

def get_current_time() -> dict:
    """Returns the current date and time."""
    from datetime import datetime
    return {"current_date": f"{datetime.now().strftime('%Y-%m-%d')}", "current_time": f"{datetime.now().strftime('%H:%M:%S')}"}

root_agent = Agent(
    name="fia_assistant_agent",
    model="gemini-2.0-flash",
    description="A specialized assistant for Fire Industry Academy (FIA) inquiries",
    instruction=FIA_ASSISTANT_INSTRUCTION,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=os.getenv("FIA_MCP_URL", "https://fia-axcelerate-mcp-905053609184.us-central1.run.app/mcp"),
                timeout=30
            ),
            tool_filter=["get_courses", "get_cohorts", "get_recorded_webinars", "search_cohorts"]
        ),
        get_current_time
    ]
)