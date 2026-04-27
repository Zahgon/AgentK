import os
from langchain_core.tools import tool

@tool
def write_to_file(file: str, file_contents: str) -> str:
    """Write the contents to a new file, will not overwrite an existing file."""
    pass
