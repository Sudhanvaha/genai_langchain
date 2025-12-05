import os
from google import genai
from google.genai.types import EmbedContentConfig

# Load Gemini API key from .env
from dotenv import load_dotenv
load_dotenv()

# Make sure you have set GEMINI_API_KEY in your .env
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Your documents
documents = [
    "Delhi is the capital of India",
    "Bengaluru is the capital of Karnataka",
    "Paris is the capital of France"
]

# Get embeddings
response = client.models.embed_content(
    model="models/embedding-001",   # Gemini embedding model
    contents=documents,
    config=EmbedContentConfig(
        output_dimensionality=32    # same as you did with OpenAI
    )
)

# Each embedding corresponds to one document
embeddings = response.embeddings

print(embeddings)


# from langchain_opeai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

# documents=["Delhi is the capital of India",
#            "Bengaluru is the capital of karnataka",
#            "Paris is the capital of France"]

# result=embedding.embed_documents(documents)

# print(str(result))

