from langchain_core.tools import tool

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@tool
def fetch_web_page_raw_html(url: str) -> str:
    """Fetches the raw HTML of a web page. If a CSS selector is provided, returns only the matching elements."""
    pass
