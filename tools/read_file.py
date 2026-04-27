from langchain_core.tools import tool

@tool

def read_file(file_path: str) -> str:
    """Returns the content of the file at the given file path."""
    pass
