# Enterprise AI Advisor

Enterprise AI Advisor is a Retrieval-Augmented Generation (RAG) application that helps IT leaders, engineers, and business users make informed decisions about enterprise AI adoption.

The app answers questions about enterprise AI tools, governance, RAG architecture, embeddings, vector databases, LangChain, LangGraph, and tool selection. It retrieves relevant content from a curated enterprise AI knowledge base and generates grounded answers with citations.

## Project Goal

My RAG app helps IT leaders, engineers, and business teams answer enterprise AI adoption, governance, and architecture questions from a curated enterprise AI knowledge base through a Streamlit chatbot with grounded answers and source citations.

## Features

- Curated enterprise AI knowledge base
- Document ingestion from markdown files
- Chunking with LangChain text splitters
- OpenAI embeddings
- ChromaDB vector store
- Retrieval-based context generation
- OpenAI-powered answer generation
- Source citations
- Failure handling for unsupported questions
- Streamlit user interface
- LangGraph workflow for agentic orchestration

## Example Questions

- What is RAG?
- What are embeddings?
- What is LangGraph?
- Should I use RAG or fine-tuning?
- Should I use ChatGPT or Copilot?
- Claude vs ChatGPT
- How should organizations govern AI?
- What controls should we put in place before rolling out AI tools?
- What is my employee ID?

## Project Structure

```text
enterprise-ai-advisor/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│   ├── raw_docs/
│   └── processed/
│
├── docs/
│   └── project_documentation.md
│
├── evaluation/
│   └── test_questions.csv
│
├── src/
│   ├── config.py
│   ├── ingest.py
│   ├── chunk.py
│   ├── embed.py
│   ├── retrieve.py
│   ├── generate.py
│   ├── graph.py
│   └── prompts.py
│
└── vectorstore/