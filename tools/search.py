from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool

_search = TavilySearchResults()

@tool
def web_search(query: str):
    """Search the web for real-time information."""
    return _search.invoke(query)
