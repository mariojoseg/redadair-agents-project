import os

from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams

from .prompt import RAG_AGENT_INSTRUCTION
from dotenv import load_dotenv

load_dotenv(override=True)

root_agent = Agent(
    name="rag_agent",
    model="gemini-1.5-pro",
    description="An agent that retrieves documents from a RAG corpus.",
    instruction=RAG_AGENT_INSTRUCTION,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url="http://0.0.0.0:8080/mcp",
                timeout=30
            )
        )
    ]
)