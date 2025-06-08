# LLMWorks

Welcome to **LLMWorks**, a collection of AI-powered applications built with LangChain, OpenAI APIs, and Streamlit. These tools enable interactive chatbot conversations, mood-based inspirational quotes, and semantic querying of PDF documents leveraging state-of-the-art language models and vector databases.

---

## Table of Contents

- [Overview](#overview)
- [Applications](#applications)
  - [AI Chat Interface](#ai-chat-interface)
  - [Mood-Based Inspiration Generator](#mood-based-inspiration-generator)
  - [PDF Query Tool Using LangChain, Astra DB, and OpenAI](#pdf-query-tool-using-langchain-astra-db-and-openai)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

LLMWorks features three distinct applications demonstrating the power of large language models integrated with LangChain and vector search technologies:

- **AI Chat Interface:** Streamlit app for conversational interaction with GPT-3.5-turbo.
- **Mood-Based Inspiration Generator:** Provides personalized motivational quotes and explanations based on user mood.
- **PDF Query Tool:** Enables semantic search inside PDF documents using embeddings stored in Astra DB Cassandra.

---

## Applications

### AI Chat Interface

A simple chatbot interface using LangChain and OpenAI GPT-3.5-turbo model.

- Clean, responsive Streamlit UI.
- Secure API key handling via `.env`.
- Button-triggered user input and model responses.

### Mood-Based Inspiration Generator

Generates motivational quotes tailored to your current mood, plus a concise explanation.

- User inputs mood.
- Generates quote using LangChain prompts.
- Provides a 3-bullet explanation of the quote’s meaning.
- Uses SequentialChain to link prompts.

### PDF Query Tool Using LangChain, Astra DB, and OpenAI

Allows semantic querying of PDF content by:

- Extracting text from PDFs.
- Chunking text for efficient embeddings.
- Generating embeddings with OpenAI.
- Storing vectors in Astra DB Cassandra.
- Performing semantic search with LangChain and OpenAI LLM.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/LLMWorks.git
cd LLMWorks
```

### 2. Create a `.env` File

Store your API keys securely by creating a `.env` file in the root directory and adding:

```env
OPENAI_API_KEY=your-openai-api-key
ASTRA_DB_APPLICATION_TOKEN=your-astra-token
ASTRA_DB_ID=your-astra-database-id
```

### 3. Install Dependencies
Install required packages using:

```bash
pip install -r requirements.txt
```

## Usage 
### Run AI Chat Interface
```bash
streamlit run llm_chatbot_tool/llm_chatbot_app.py
```

### Run Mood-Based Inspiration Generator
```bash
streamlit run llm_recommender_app_tool/llm_recommender_app.py
```
### Run PDF Query Tool
```bash
python semantic_pdf_query_tool/semantic_pdf_query_app.py
```

## Contributing
Contributions are welcome! Please open issues or submit pull requests to enhance functionality, fix bugs, or improve documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
