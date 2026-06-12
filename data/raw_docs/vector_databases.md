# Vector Databases

## What is a Vector Database?

A vector database stores embeddings and allows applications to search for similar vectors.

In RAG applications, vector databases are used to retrieve document chunks that are semantically similar to a user's question.

## Common Vector Databases

Examples include:

- ChromaDB
- Pinecone
- Weaviate
- Qdrant
- PostgreSQL with pgvector

## Why Use a Vector Database?

Vector databases help with:

- Semantic search
- Fast retrieval
- Similarity matching
- Scalable knowledge search

## Enterprise Considerations

Organizations should evaluate:

- Scale
- Cost
- Security
- Latency
- Integration with existing systems

## Advisor Notes

For prototypes and small projects, ChromaDB is simple and effective. For enterprise production workloads, teams may consider managed vector databases or PostgreSQL with pgvector.