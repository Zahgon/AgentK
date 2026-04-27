from langchain_core.tools import tool
from langchain_community.document_loaders.url_selenium import SeleniumURLLoader

@tool
def fetch_web_page_content(url: str):
    """Fetch content from a web page."""
    pass
