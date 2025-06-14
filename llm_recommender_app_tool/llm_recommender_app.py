import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import streamlit as st
from dotenv import load_dotenv
from openai_key import another_key

# Load environment config
load_dotenv()
#os.environ['OPENAI_API_KEY'] = another_key

# Initialize language model
llm = OpenAI(temperature=0.7)

# Define prompt templates
# First prompt: Ask for a motivational quote based on user's mood
mood_prompt = PromptTemplate(
    input_variables=['mood'],
    template="I'm feeling {mood} today. Could you share an inspiring quote that fits this mood? Just provide the quote."
)
mood_chain = LLMChain(llm=llm, prompt=mood_prompt, output_key='quote')

# Second prompt: Ask for a brief explanation about the quote
explanation_prompt = PromptTemplate(
    input_variables=['quote'],
    template="Explain the meaning of this quote briefly in 3 bullet points:\n{quote}"
)
explanation_chain = LLMChain(llm=llm, prompt=explanation_prompt, output_key='explanation')

# Combine the chains sequentially
inspiration_chain = SequentialChain(
    chains=[mood_chain, explanation_chain],
    input_variables=['mood'],
    output_variables=['quote', 'explanation']
)

# Streamlit app setup
st.set_page_config(page_title="Mood-based Inspiration Generator")
st.title("Get Inspired According to Your Mood")

user_mood = st.text_input("How are you feeling right now?")
generate = st.button("Generate Inspiration")

if generate and user_mood:
    result = inspiration_chain({'mood': user_mood})
    st.subheader("Your Quote:")
    st.write(result['quote'])

    st.subheader("What It Means:")
    st.write(result['explanation'])
