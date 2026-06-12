from typing import TypedDict

from langgraph.graph import StateGraph, END

from generate import generate_answer


class AdvisorState(TypedDict):
    question: str
    intent: str
    answer: str
    sources: list


def classify_intent(state: AdvisorState):
    question = state["question"].lower()

    if "copilot" in question or "chatgpt" in question or "claude" in question:
        intent = "Tool Selection"
    elif "govern" in question or "security" in question or "privacy" in question:
        intent = "Governance"
    elif "rag" in question or "fine-tuning" in question or "embedding" in question or "vector" in question:
        intent = "AI Engineering"
    elif "langgraph" in question or "agent" in question:
        intent = "Agentic Workflow"
    else:
        intent = "General"

    return {"intent": intent}


def generate_response(state: AdvisorState):
    answer, sources = generate_answer(state["question"])

    return {
        "answer": answer,
        "sources": sources
    }


def build_graph():
    graph = StateGraph(AdvisorState)

    graph.add_node("classify_intent", classify_intent)
    graph.add_node("generate_response", generate_response)

    graph.set_entry_point("classify_intent")

    graph.add_edge("classify_intent", "generate_response")
    graph.add_edge("generate_response", END)

    return graph.compile()


if __name__ == "__main__":
    app = build_graph()

    question = input("Ask Enterprise AI Advisor: ")

    result = app.invoke(
        {
            "question": question,
            "intent": "",
            "answer": "",
            "sources": []
        }
    )

    print("\nIntent:")
    print(result["intent"])

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print(f"- {source}")