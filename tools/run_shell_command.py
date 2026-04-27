import subprocess
from langchain_core.tools import tool

@tool
def run_shell_command(command: str):
    """Run a shell command and return the output."""
    pass
