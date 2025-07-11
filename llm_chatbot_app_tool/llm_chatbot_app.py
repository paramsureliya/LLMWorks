import os
import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv
from openai_key import another_key  # Import your API key securely from this module

# Load environment configurations
load_dotenv()
#os.environ['OPENAI_API_KEY'] = another_key  # Assign API key to environment variable

def generate_reply(prompt: str) -> str:
    """
    Obtain a response from OpenAI's language model for a given prompt.
    
    Args:
        prompt (str): The input query from the user.

    Returns:
        str: The text response generated by the language model.
    """
    language_model = OpenAI(model_name="gpt-3.5-turbo-1106", temperature=0.6)
    return language_model(prompt)

# Set up Streamlit interface
st.set_page_config(page_title="AI Chat Interface", page_icon="🤖")
st.header("Interactive AI Chatbot")

# Input widget for user to type their query
question_input = st.text_input("Ask me anything:", key="user_query")
trigger = st.button("Send")

# Generate and display output after user submission
if trigger and question_input:
    answer = generate_reply(question_input)
    st.subheader("AI's Answer:")
    st.write(answer)
