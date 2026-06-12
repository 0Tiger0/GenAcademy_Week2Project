import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

from config import VECTORSTORE_DIR, TOP_K

load_dotenv()

client = OpenAI()

EMBEDDING_MODEL = os.getenv(
    "OPENAI_EMBEDDING_MODEL",
    "text-embedding-3-small"
)


def embed_query(query: str):
    """
    Create an embedding for the user query using OpenAI embeddings.
    """

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query
    )

    return response.data[0].embedding


def retrieve(query: str):
    """
    Retrieve the most relevant chunks from ChromaDB for a user query.
    """

    client_db = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))
    collection = client_db.get_collection(name="enterprise_ai_advisor")

    query_embedding = embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )

    return results


if __name__ == "__main__":
    user_query = input("Ask a question: ")

    results = retrieve(user_query)

    print(f"\nQuery: {user_query}\n")

    for i, doc in enumerate(results["documents"][0]):
        print(f"Result {i + 1}")
        print(f"Source: {results['metadatas'][0][i]['filename']}")
        print(f"Content: {doc[:500]}")
        print("-" * 50)