j

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

class MyState(TypedDict):
    steps: List[str]
    x: int

def add_one(state: MyState):
    return {"x": state["x"] + 5, "steps": state["steps"]+ ["add_one"]}

def double(state: MyState):
    return {"x": state["x"] * 2, "steps": state["steps"] + ["double"]}

def tru(state: MyState):
    return {"x": state["x"] - 3, "steps": state["steps"]+ ["tru"]}


g = StateGraph(MyState)
g.add_node("add_one", add_one)
g.add_node("double", double)
g.add_node("tru", tru)
g.add_edge(START, "add_one")
g.add_edge("add_one", "double")
g.add_edge("double","tru")
g.add_edge("tru", END)

app = g.compile()
print(app.invoke({"x": 2, "steps": []}))
