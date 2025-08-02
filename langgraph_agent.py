from langgraph.graph import StateGraph, END
from typing import TypedDict
from ollama_model import get_ollama_model
from nodes.calendar_node import add_event_to_calendar_node
from nodes.email_node import summarize_email_node
from nodes.note_node import add_note_to_file_node


# Define state schema
class AgentState(TypedDict):
    input: str
    output: str


# Create the LLM that routes the request
llm = get_ollama_model()


def router(state: AgentState) -> dict:
    # Use the LLM to determine which tool to use
    input_text = state["input"]
    response = llm.invoke(
        f"Given the input: '{input_text}', respond ONLY with one word: either 'email', 'calendar', 'notes', or 'none' if it doesn't belong to any category."
    )
    destination = response.strip().lower()
    return {
        "next": destination,
        "input": input_text
    }


def noop_node(state: AgentState) -> dict:
    return {"output": "Haha, I’m not sure what you want me to do with that. Try again with a real request 😅"}


# Build graph
builder = StateGraph(AgentState)
builder.add_node("router", router)
builder.add_node("email", summarize_email_node)
builder.add_node("calendar", add_event_to_calendar_node)
builder.add_node("notes", add_note_to_file_node)
builder.add_node("noop", noop_node)

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    lambda state: state["next"],
    {
        "email": "email",
        "calendar": "calendar",
        "notes": "notes",
        "none": "noop"
    }
)

builder.add_edge("email", END)
builder.add_edge("calendar", END)
builder.add_edge("notes", END)
builder.add_edge("noop", END)

graph = builder.compile()
