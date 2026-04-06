from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state["messages"]

    system_prompt = SystemMessage(
        content="You are a helpful assistant. Answer naturally and do not repeat user input."
    )

    response = llm.invoke([system_prompt] + messages)

    return {"messages": [response]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)