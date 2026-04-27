import sys
import traceback
from langchain_core.tools import tool
import utils

@tool
def assign_agent_to_task(agent_name: str, task: str):
    """Assign an agent to a task. This function returns the response from the agent."""
    pass
