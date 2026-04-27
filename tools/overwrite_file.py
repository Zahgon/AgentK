from langchain_core.tools import tool

@tool
def overwrite_file(file_path: str, content: str) -> str:
    """Replaces the file at the given path with the given content, returning a string message confirming success."""
    pass
