
# pdf_query_tool.py

from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
import cassio
import os

# Load API Keys (Ensure you set these in your environment variables or a config file)
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Astra DB
cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

# Load LLM and Embeddings
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
embed = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Initialize vector store
astra_vector_store = Cassandra(
    embedding=embed,
    table_name="qa_demo",
    session=None,
    keyspace=None,
)

# Load PDF file and extract text
pdf_path = "CNN_research_paper.pdf"  # Change this to the path of your PDF file
pdf_reader = PdfReader(pdf_path)

raw_text = ""
for page in pdf_reader.pages:
    content = page.extract_text()
    if content:
        raw_text += content

# Split text into chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(raw_text)

# Add text chunks to the vector store
astra_vector_store.add_texts(texts)
astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# Query Function
def query_pdf(question: str):
    """Queries the stored PDF data using LLM"""
    answer = astra_vector_index.query(question=question, llm=llm)
    return answer

# Example usage
if __name__ == "__main__":
    user_question = "Are CNNs better than ANNs at predictive maintenance?"
    response = query_pdf(user_question)
    print("Response:", response)
