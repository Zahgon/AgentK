from typing import Literal

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode

import config

system_prompt = """You are web_researcher, a ReAct agent that can use the web to research answers.

You have a tool to search the web, and a tool to fetch the content of a web page.
```
"""
    
from tools.duck_duck_go_web_search import duck_duck_go_web_search
from tools.fetch_web_page_content import fetch_web_page_content

tools = [duck_duck_go_web_search, fetch_web_page_content]

def reasoning(state: MessagesState):
    pass

def check_for_tool_calls(state: MessagesState) -> Literal["tools", END]:
    pass

acting = ToolNode(tools)

workflow = StateGraph(MessagesState)
workflow.add_node("reasoning", reasoning)
workflow.add_node("tools", acting)
workflow.set_entry_point("reasoning")
workflow.add_conditional_edges(
    "reasoning",
    check_for_tool_calls,
)
workflow.add_edge("tools", 'reasoning')

graph = workflow.compile()


def web_researcher(task: str) -> str:
    """Researches the web."""
    pass
