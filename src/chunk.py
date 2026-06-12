from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP
from ingest import load_documents


def chunk_documents():
    """
    Split loaded documents into smaller chunks for embedding and retrieval.
    """

    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for doc in docs:
        split_texts = splitter.split_text(doc["content"])

        for i, text in enumerate(split_texts):
            chunks.append(
                {
                    "id": f"{doc['filename']}_chunk_{i}",
                    "filename": doc["filename"],
                    "chunk_index": i,
                    "content": text
                }
            )

    return chunks


if __name__ == "__main__":
    chunks = chunk_documents()

    print(f"\nCreated {len(chunks)} chunk(s)\n")

    for chunk in chunks:
        print(f"Chunk ID: {chunk['id']}")
        print(f"Source: {chunk['filename']}")
        print(f"Preview: {chunk['content'][:200]}")
        print("-" * 50)