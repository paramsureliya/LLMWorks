# Mood-Based Inspiration Generator

This is a simple Streamlit web app that provides users with an inspiring quote based on their current mood, along with a brief explanation of the quote.

---

## Features

- **Mood input:** Users enter how they are feeling.
- **Motivational quote:** The app generates a quote tailored to the user's mood.
- **Quote explanation:** A short 3-bullet summary explaining the meaning of the quote.

---

## How It Works

1. The app uses **LangChain's** `OpenAI` wrapper to interact with OpenAI's language models.
2. It defines two prompt templates:
   - One to request a motivational quote based on the user’s mood.
   - Another to explain the meaning of the generated quote in bullet points.
3. These prompts are linked using a **SequentialChain** which passes the output of the first prompt (`quote`) as input to the second.
4. The user interacts with the app via Streamlit UI.

---

## Setup Instructions

### 1. API Key Configuration

Create a `.env` file in your project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your-openai-api-key
