from langchain_core.messages import HumanMessage
from agent.graph import build_graph

def run():
    graph = build_graph()

    inputs = {
        "messages": [
            HumanMessage(
                content="What's the weather in Zurich and what should I wear?"
            )
        ]
    }

    for step in graph.stream(inputs, stream_mode="values"):
        step["messages"][-1].pretty_print()

if __name__ == "__main__":
    run()
