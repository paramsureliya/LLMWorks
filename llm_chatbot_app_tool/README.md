# 🤖 AI Chat Interface

This is a simple Streamlit web app that allows users to interact with OpenAI's language model using natural language prompts. The app uses the LangChain framework to interface with OpenAI's GPT-3.5-turbo model.

---

## 🔐 API Key Configuration

To securely access the OpenAI API, you'll need to provide your API key. 

Create a `.env` file in the root of your project directory and add the following line:

```env
OPENAI_API_KEY=your-openai-api-key
```

## 🔧 Features

- Clean and responsive Streamlit UI
- Uses LangChain's OpenAI wrapper for model access
- Loads API key securely via `dotenv` and a custom Python module
- Asynchronous-like behavior with button-based interaction
- Easily customizable for different prompt styles or applications

---

## 🧠 How It Works

1. The user types a message into the input box.
2. Upon clicking the **Send** button, the message is passed to the `generate_reply()` function.
3. The function queries OpenAI's GPT-3.5-turbo model using LangChain.
4. The model's response is displayed below the input box in the Streamlit interface.

---