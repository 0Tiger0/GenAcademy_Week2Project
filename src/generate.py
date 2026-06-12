import os

from dotenv import load_dotenv
from openai import OpenAI

from retrieve import retrieve

load_dotenv()

client = OpenAI()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def build_context(results):
    """
    Build a context string from retrieved ChromaDB results
    and collect unique source filenames.
    """

    context_blocks = []
    sources = []

    for i, doc in enumerate(results["documents"][0]):
        metadata = results["metadatas"][0][i]
        source = metadata["filename"]

        context_blocks.append(
            f"Source: {source}\nContent:\n{doc}"
        )

        if source not in sources:
            sources.append(source)

    context = "\n\n---\n\n".join(context_blocks)

    return context, sources


def generate_answer(question: str):
    """
    Retrieve relevant context and generate a grounded advisor answer.
    """

    results = retrieve(question)
    context, sources = build_context(results)

    prompt = f"""
You are Enterprise AI Advisor, an AI consultant for IT leaders and engineers.

Your job is to answer the user's question using the retrieved context.

Important rules:
- If the retrieved context contains information that answers the question, answer it.
- Do not refuse when the context clearly contains the answer.
- If the user asks a "What is..." question, provide a clear definition.
- If the user asks a comparison question such as "Claude vs ChatGPT", compare the options and recommend when to use each.
- If the user asks for an architecture recommendation or internal knowledge assistant design, include the key RAG components: documents, chunking, embeddings, vector database, retrieval, answer generation, and citations.
- If the user asks an advisory question, provide a recommendation and reasoning.
- Use only the retrieved context.
- Cite exact source filenames from the context.

Only refuse if the retrieved context does not contain information that answers the question.

If the answer is unsupported, say exactly:
I could not find that information in the knowledge base.

User question:
{question}

Retrieved context:
{context}

If the answer is supported, answer in this format:

Recommendation:
Reasoning:
Sources: list only the exact source filenames from the context, such as example.md

If the question is asking for a simple definition, the Recommendation can be a direct definition.
"""

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt
    )

    answer = response.output_text.strip()

    if "could not find that information" in answer.lower():
        return answer, []

    used_sources = [
        source for source in sources
        if source in answer
    ]

    if used_sources:
        return answer, used_sources

    return answer, sources


if __name__ == "__main__":
    question = input("Ask Enterprise AI Advisor: ")

    answer, sources = generate_answer(question)

    print("\nAnswer:\n")
    print(answer)

    if sources:
        print("\nRetrieved Sources:")
        for source in sources:
            print(f"- {source}")
    else:
        print("\nNo source citations shown because the answer was not found in the knowledge base.")