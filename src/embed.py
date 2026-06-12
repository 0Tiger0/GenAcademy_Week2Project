import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

from chunk import chunk_documents
from config import VECTORSTORE_DIR

load_dotenv()

client = OpenAI()

EMBEDDING_MODEL = os.getenv(
    "OPENAI_EMBEDDING_MODEL",
    "text-embedding-3-small"
)


def embed_texts(texts):
    """
    Create embeddings using OpenAI embeddings API.
    """

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    embeddings = [
        item.embedding
        for item in sorted(response.data, key=lambda x: x.index)
    ]

    return embeddings


def create_vectorstore():
    """
    Create embeddings and store document chunks in ChromaDB.
    """

    chunks = chunk_documents()

    client_db = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))

    try:
        client_db.delete_collection("enterprise_ai_advisor")
    except Exception:
        pass

    collection = client_db.create_collection(
        name="enterprise_ai_advisor"
    )

    ids = []
    documents = []
    metadatas = []

    for chunk in chunks:
        ids.append(chunk["id"])
        documents.append(chunk["content"])
        metadatas.append(
            {
                "filename": chunk["filename"],
                "chunk_index": chunk["chunk_index"]
            }
        )

    embeddings = embed_texts(documents)

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    print(f"\nStored {len(chunks)} chunk(s) in ChromaDB")
    print(f"Embedding model: {EMBEDDING_MODEL}\n")


if __name__ == "__main__":
    create_vectorstore()