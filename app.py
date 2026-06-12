import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).parent
SRC_DIR = PROJECT_ROOT / "src"
sys.path.append(str(SRC_DIR))

st.set_page_config(
    page_title="Enterprise AI Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("Enterprise AI Advisor")

st.write(
    "Ask questions about enterprise AI tools, governance, RAG, LangChain, LangGraph, and AI architecture."
)

with st.form("advisor_form"):
    question = st.text_area(
        "Ask Enterprise AI Advisor",
        placeholder="Example: Should I use RAG or fine-tuning?",
        height=100
    )

    submitted = st.form_submit_button("Submit")

if submitted and question:
    with st.spinner("Thinking..."):
        from generate import generate_answer

        answer, sources = generate_answer(question)

    st.subheader("Answer")
    st.markdown(answer)

    if sources:
        st.subheader("Retrieved Sources")
        for source in sources:
            st.write(f"- {source}")
    else:
        st.info("No source citations shown because the answer was not found in the knowledge base.")