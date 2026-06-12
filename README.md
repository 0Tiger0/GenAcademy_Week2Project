# Enterprise AI Advisor

Enterprise AI Advisor is a Retrieval-Augmented Generation (RAG) application that helps IT leaders, engineers, and business users make informed decisions about enterprise AI adoption.

The app answers questions about enterprise AI tools, governance, RAG architecture, embeddings, vector databases, LangChain, LangGraph, and tool selection. It retrieves relevant content from a curated enterprise AI knowledge base and generates grounded answers with source citations.

---

## Project Goal

My RAG app helps IT leaders, engineers, and business teams answer enterprise AI adoption, governance, and architecture questions from a curated enterprise AI knowledge base through a Streamlit chatbot with grounded answers and source citations.

---

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
- Nebius Token Factory smoke test for course requirement

---

## Example Questions

The app can answer questions such as:

- What is RAG?
- What are embeddings?
- What is LangChain?
- What is LangGraph?
- What is Microsoft Copilot?
- Should I use RAG or fine-tuning?
- Should I use ChatGPT or Copilot?
- Claude vs ChatGPT
- How should organizations govern AI?
- What controls should we put in place before rolling out AI tools?
- Our company wants an internal knowledge assistant. What architecture should we use?
- When would LangGraph be better than a simple RAG chain?

The app also handles unsupported questions, such as:

- What is my employee ID?
- What is the weather tomorrow?
- What is Kuruvilla's favorite food?

Expected unsupported response:

```text
I could not find that information in the knowledge base.
```

---

## Project Structure

```text
enterprise-ai-advisor/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   ├── raw_docs/
│   └── processed/
│
├── docs/
│   ├── project_documentation.md
│   └── demo_script.md
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
│   ├── nebius_test.py
│   └── prompts.py
│
└── vectorstore/
```

Note:

```text
.env
venv/
vectorstore/
__pycache__/
```

are ignored by Git and should not be committed.

---

## Architecture

The application follows a standard RAG pipeline:

```text
User Question
   ↓
Embed Question
   ↓
Retrieve Relevant Chunks from ChromaDB
   ↓
Build Context
   ↓
Generate Grounded Answer
   ↓
Return Answer + Source Citations
```

The LangGraph workflow adds an agentic structure:

```text
Question
   ↓
Intent Classification
   ↓
Answer Generation
   ↓
Return Sources
```

---

## Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- ChromaDB
- OpenAI API
- OpenAI Embeddings
- Nebius Token Factory
- python-dotenv
- pandas

---

## Knowledge Corpus

The knowledge base is stored in:

```text
data/raw_docs/
```

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

Example corpus files:

```text
chatgpt_enterprise_overview.md
chatgpt_enterprise_security.md
chatgpt_vs_copilot.md
claude_vs_chatgpt.md
copilot_overview.md
copilot_security.md
rag_fundamentals.md
embeddings.md
vector_databases.md
fine_tuning_vs_rag.md
langchain_intro.md
langgraph_intro.md
enterprise_ai_governance.md
```

---

## Environment Variables

Create a local `.env` file in the project root.

Use `.env.example` as the template:

```text
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

NEBIUS_API_KEY=your_nebius_api_key_here
NEBIUS_MODEL=meta-llama/Llama-3.3-70B-Instruct
```

Important:

```text
Do not commit .env to GitHub.
```

Only `.env.example` should be committed.

---

## Setup Instructions

### 1. Clone the repository

```powershell
git clone https://github.com/0Tiger0/GenAcademy_Week2Project.git
cd GenAcademy_Week2Project
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Create `.env`

Copy `.env.example` to `.env` and add your real API keys.

```powershell
copy .env.example .env
```

Then edit `.env` with your real keys.

### 6. Build the vector database

```powershell
python src\embed.py
```

This reads documents from:

```text
data/raw_docs/
```

chunks them, embeds them, and stores vectors in:

```text
vectorstore/
```

### 7. Run the Streamlit app

```powershell
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## Running Individual Pipeline Steps

### Test ingestion

```powershell
python src\ingest.py
```

### Test chunking

```powershell
python src\chunk.py
```

### Build embeddings and vector store

```powershell
python src\embed.py
```

### Test retrieval

```powershell
python src\retrieve.py
```

### Test answer generation

```powershell
python src\generate.py
```

### Test LangGraph workflow

```powershell
python src\graph.py
```

### Test Nebius Token Factory call

```powershell
python src\nebius_test.py
```

Expected Nebius output:

```text
Nebius Token Factory model call worked.
```

---

## Nebius Token Factory Requirement

The course requires using Nebius Token Factory for at least one model call.

This project includes a Nebius smoke-test script:

```text
src/nebius_test.py
```

The main Streamlit RAG app uses OpenAI embeddings and OpenAI answer generation for stability. The Nebius script verifies Token Factory integration separately without breaking the working Streamlit application.

Nebius model used:

```text
meta-llama/Llama-3.3-70B-Instruct
```

Run the smoke test:

```powershell
python src\nebius_test.py
```

Expected output:

```text
Nebius Token Factory smoke test completed.
Model used: meta-llama/Llama-3.3-70B-Instruct

Nebius Token Factory model call worked.
```

---

## Evaluation

Evaluation questions are stored in:

```text
evaluation/test_questions.csv
```

The project was tested against 18 questions:

```text
Easy questions: 5
Medium questions: 5
Hard questions: 5
Failure cases: 3
```

Final result:

```text
18 / 18 Passed
```

Evaluation categories:

| Category | Count | Status |
|---|---:|---|
| Easy | 5 | Passed |
| Medium | 5 | Passed |
| Hard | 5 | Passed |
| Failure | 3 | Passed |

Failure questions tested:

```text
What is Kuruvilla's favorite food?
What is my employee ID?
What is the weather tomorrow?
```

Expected fallback response:

```text
I could not find that information in the knowledge base.
```

---

## Example Outputs

### Example 1: RAG vs Fine-Tuning

Question:

```text
Should I use RAG or fine-tuning?
```

Expected behavior:

The app recommends RAG when knowledge changes frequently, answers need citations, and responses must be grounded in trusted documents. It explains that fine-tuning is more appropriate for repeated patterns, style, or output formatting.

Expected sources:

```text
fine_tuning_vs_rag.md
rag_fundamentals.md
```

---

### Example 2: ChatGPT vs Copilot

Question:

```text
Should I use ChatGPT or Copilot?
```

Expected behavior:

The app explains that ChatGPT is useful for flexible enterprise AI workflows, while Copilot is better when the organization already works heavily in Microsoft 365.

Expected source:

```text
chatgpt_vs_copilot.md
```

---

### Example 3: Failure Handling

Question:

```text
What is my employee ID?
```

Expected answer:

```text
I could not find that information in the knowledge base.
```

The app does not show unrelated source citations for unsupported answers.

---

## Key Design Decisions

### Markdown corpus

The corpus uses curated markdown documents instead of PDFs to make ingestion, chunking, and retrieval more reliable for the Week 2 project.

### OpenAI embeddings

The project originally tested local SentenceTransformer embeddings, but local Torch and Transformers dependencies caused Streamlit startup issues.

The final app uses:

```text
text-embedding-3-small
```

This made the app more stable and easier to demo.

### ChromaDB vector store

ChromaDB was selected because it is simple, local, and appropriate for a bootcamp-scale RAG project.

### Source citation filtering

The first version showed all retrieved sources. The final version filters citations so the UI only shows sources used in the model-generated answer.

### Failure handling

Unsupported questions return a refusal message and hide unrelated sources.

---

## Project Documentation

Additional documentation is available in:

```text
docs/project_documentation.md
```

Demo script:

```text
docs/demo_script.md
```

Evaluation report:

```text
evaluation/test_questions.csv
```

---

## Known Limitations

- The corpus is curated and small compared to a real enterprise knowledge base.
- The app uses dense retrieval only, not hybrid retrieval.
- The Streamlit UI calls the stable generation pipeline directly.
- The LangGraph workflow is implemented and tested separately in the terminal.
- The vector store is local and should be rebuilt after cloning.

---

## Future Improvements

- Add hybrid retrieval with BM25 + vector search
- Add reranking
- Add document upload support
- Add Slack or Teams integration
- Add SharePoint or Confluence connectors
- Add user authentication
- Add LangSmith tracing
- Add automated RAGAS evaluation
- Add confidence scoring
- Deploy to cloud

---

## Author

Kuruvilla Abraham