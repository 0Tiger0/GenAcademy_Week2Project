# Fine-Tuning vs RAG

## Overview

Fine-tuning and Retrieval-Augmented Generation are two different approaches for improving large language model performance.

## Fine-Tuning

Fine-tuning updates a model using training examples.

It is useful when the model needs to learn a specific style, format, classification pattern, or repeated task behavior.

## RAG

RAG retrieves external information at query time and provides it to the language model as context.

It is useful when answers must be grounded in documents, policies, product information, or frequently changing knowledge.

## When to Use Fine-Tuning

Use fine-tuning when:

- The task has repeated patterns
- The output format must be consistent
- You have many high-quality training examples
- The knowledge does not change frequently

## When to Use RAG

Use RAG when:

- The system needs current information
- Answers must cite sources
- Knowledge changes often
- The assistant must answer from trusted documents

## Advisor Notes

Most enterprise knowledge assistants should start with RAG before fine-tuning because RAG is easier to update, easier to cite, and safer for changing documentation.