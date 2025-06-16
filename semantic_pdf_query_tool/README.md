# PDF Query Tool Using LangChain, Astra DB, and OpenAI

This Python script allows you to query the content of a PDF document by leveraging OpenAI's language models, LangChain vector stores, and Astra DB (Cassandra) for vector embedding storage and retrieval.

---

## Overview

- Reads a PDF file and extracts its text content.
- Splits the extracted text into smaller chunks.
- Converts text chunks into embeddings using OpenAI embeddings.
- Stores embeddings in Astra DB via Cassandra vector store.
- Enables semantic querying of the PDF content through LangChain's vector index and OpenAI LLM.

---

## Features

- **PDF text extraction:** Uses `PyPDF2` to read and extract text.
- **Text chunking:** Splits long documents into overlapping chunks for better embedding representation.
- **Vector embeddings:** Uses OpenAI's embedding models.
- **Persistent storage:** Stores embeddings in Astra DB Cassandra for scalable, persistent vector search.
- **Semantic search:** Queries the vector store with a natural language question, answered by the LLM based on relevant PDF content.

---

## Setup Instructions

### 1. Environment Variables

Store your sensitive API keys and tokens securely as environment variables:

```bash
export ASTRA_DB_APPLICATION_TOKEN=your_astra_token
export ASTRA_DB_ID=your_astra_database_id
export OPENAI_API_KEY=your_openai_api_key
