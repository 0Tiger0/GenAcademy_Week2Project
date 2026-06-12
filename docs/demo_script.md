# Enterprise AI Advisor Demo Script

## Video Goal

Show a working Retrieval-Augmented Generation (RAG) application that helps users answer enterprise AI adoption, governance, and architecture questions using a curated knowledge base with citations.

Target video length: 5 minutes or less.

---

## 0:00 – 0:30 Introduction

Hi, my name is Kuruvilla Abraham, and this is my Week 2 project for the Mastering Agentic AI course.

My project is called Enterprise AI Advisor.

It is a RAG-powered application that helps IT leaders, engineers, and business users answer questions about enterprise AI tools, governance, RAG architecture, embeddings, vector databases, LangChain, and LangGraph.

The goal is to provide grounded answers from a curated knowledge base instead of relying only on the model's general knowledge.

---

## 0:30 – 1:00 One-Line RAG Statement

My RAG app helps IT leaders, engineers, and business teams answer enterprise AI adoption, governance, and architecture questions from a curated enterprise AI knowledge base through a Streamlit chatbot with grounded answers and source citations.

---

## 1:00 – 1:45 Project Architecture

The application follows a standard RAG pipeline:

User Question
   ?
Embed Question
   ?
Retrieve Relevant Chunks from ChromaDB
   ?
Build Context
   ?
Generate Grounded Answer
   ?
Return Answer + Source Citations

The project includes:

- Markdown documents in data/raw_docs
- Ingestion logic in src/ingest.py
- Chunking logic in src/chunk.py
- OpenAI embeddings in src/embed.py
- ChromaDB vector storage
- Retrieval logic in src/retrieve.py
- Answer generation in src/generate.py
- Streamlit UI in app.py
- LangGraph workflow in src/graph.py

---

## 1:45 – 2:15 Corpus

The corpus contains 20 curated markdown documents covering:

- ChatGPT Enterprise
- Claude
- Microsoft Copilot
- Copilot Studio
- RAG fundamentals
- Embeddings
- Vector databases
- Fine-tuning vs RAG
- LangChain
- LangGraph
- Enterprise AI governance

The documents are stored in data/raw_docs.

---

## 2:15 – 3:30 Live Demo Questions

Demo Question 1:

Should I use RAG or fine-tuning?

Expected talking point:
The app recommends RAG when knowledge changes frequently, answers need citations, and responses should be grounded in documents.

Demo Question 2:

Should I use ChatGPT or Copilot?

Expected talking point:
The app explains that ChatGPT is better for flexible enterprise AI workflows, while Copilot is better when the organization already uses Microsoft 365.

Demo Question 3:

How should organizations govern AI?

Expected talking point:
The app recommends governance controls such as acceptable use policies, data handling guidance, access management, monitoring, training, and human oversight.

---

## 3:30 – 4:15 Architecture Question

Ask:

Our company wants an internal knowledge assistant. What architecture should we use?

Expected talking point:
The app recommends a RAG architecture and explains documents, chunking, embeddings, vector database, retrieval, answer generation, and citations.

---

## 4:15 – 4:45 Failure Handling

Ask:

What is my employee ID?

Expected result:

I could not find that information in the knowledge base.

Talking point:
This is important because a RAG app should not hallucinate when the answer is not in the retrieved documents.

The app also hides source citations for unsupported answers so it does not imply that unrelated documents support the response.

---

## 4:45 – 5:00 Evaluation and Wrap-Up

The project was evaluated with 18 test questions:

- 5 easy questions
- 5 medium questions
- 5 hard questions
- 3 failure cases

All 18 test questions passed.

The evaluation file is stored in evaluation/test_questions.csv.

The final project includes:

- Working Streamlit app
- RAG pipeline
- Source citations
- Failure handling
- LangGraph workflow
- Project documentation
- Evaluation report
- GitHub repository
