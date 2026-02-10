import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import ToolMessage

from tools.search import web_search
from tools.clothing import recommend_clothing

TOOLS = [web_search, recommend_clothing]
TOOLS_BY_NAME = {t.name: t for t in TOOLS}

model = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a reasoning agent. Think step-by-step and use tools when required."),
    MessagesPlaceholder(variable_name="messages"),
])

agent_llm = prompt | model.bind_tools(TOOLS)


def call_model(state):
    response = agent_llm.invoke({"messages": state["messages"]})
    return {"messages": [response]}


def call_tools(state):
    results = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = TOOLS_BY_NAME[tool_call["name"]]
        output = tool.invoke(tool_call["args"])
        results.append(
            ToolMessage(
                content=json.dumps(output),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": results}


def should_continue(state):
    return "continue" if state["messages"][-1].tool_calls else "end"
