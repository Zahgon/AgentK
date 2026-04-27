import os
from langchain_core.tools import tool

@tool
def delete_file(file_path: str) -> str:
    """Deletes the file at the given path and returns a string confirming success."""
    pass
