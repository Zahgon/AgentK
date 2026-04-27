import sqlite3
import importlib.util
import sys
import string
import secrets
import traceback

from langgraph.checkpoint.sqlite import SqliteSaver

conn = sqlite3.connect("checkpoints.sqlite", check_same_thread=False)
checkpointer = SqliteSaver(conn)

def all_tool_functions():
    pass

def list_broken_tools():
    pass

def list_tools():
    """
    list all tools available in the tools directory

    :return: list of tools
    """
    pass

def all_agents(exclude=["hermes"]):
    pass

def list_broken_agents():
    pass

def list_agents():
    """
    list all agents available in the agents directory

    :return: list of agents
    """
    pass

def gensym(length=32, prefix="gensym_"):
    """
    generates a fairly unique symbol, used to make a module name,
    used as a helper function for load_module

    :return: generated symbol
    """
    pass

def load_module(source, module_name=None):
    """
    reads file source and loads it as a module

    :param source: file to load
    :param module_name: name of module to register in sys.modules
    :return: loaded module
    """
    pass
