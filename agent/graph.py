from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes import call_model, call_tools, should_continue

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("agent", call_model)
    graph.add_node("tools", call_tools)

    graph.set_entry_point("agent")
    graph.add_edge("tools", "agent")

    graph.add_conditional_edges(
        "agent",
        should_continue,
        {"continue": "tools", "end": END},
    )

    return graph.compile()
