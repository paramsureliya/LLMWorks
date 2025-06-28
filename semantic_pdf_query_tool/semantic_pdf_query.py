# pdf_query_tool.py

from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
import cassio
import os

# Load API keys from environment variables (set these securely)
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize connection to Astra DB using cassio client
cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

# Initialize OpenAI LLM and embeddings with your API key
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
embed = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Set up the vector store in Astra DB to store embeddings of PDF text chunks
astra_vector_store = Cassandra(
    embedding=embed,
    table_name="qa_demo",
    session=None,
    keyspace=None,
)

# Load and read the PDF file (contains academic research on pairs trading)
pdf_path = "Pairs Trading  Performance of a Relative.pdf"  # Give PDF file path

pdf_reader = PdfReader(pdf_path)

# Extract all text from the PDF pages into one string
raw_text = ""
for page in pdf_reader.pages:
    content = page.extract_text()
    if content:
        raw_text += content

# Split the extracted text into manageable chunks for embedding
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(raw_text)

# Add the text chunks as embeddings into the Astra vector store
astra_vector_store.add_texts(texts)

# Wrap the vector store for easy querying with LangChain
astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# Define a query function to ask questions about the PDF content
def query_pdf(question: str):
    """
    Query the embedded PDF data using the LLM to get a context-aware answer.

    Parameters:
        question (str): The question you want to ask about the PDF content.

    Returns:
        str: The LLM-generated answer based on the PDF's content.
    """
    answer = astra_vector_index.query(question=question, llm=llm)
    return answer

# Example usage
if __name__ == "__main__":
    user_question = "What is the history and psychological explanation behind pairs trading?"
    response = query_pdf(user_question)
    print("Response:", response)
