from pathlib import Path

from config import RAW_DOCS_DIR


def load_documents():
    """
    Load markdown documents from raw_docs folder
    """

    documents = []

    for file_path in RAW_DOCS_DIR.glob("*.md"):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

            documents.append(
                {
                    "filename": file_path.name,
                    "content": content
                }
            )

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print(f"\nLoaded {len(docs)} document(s)\n")

    for doc in docs:
        print(f"Document: {doc['filename']}")
        print("-" * 50)