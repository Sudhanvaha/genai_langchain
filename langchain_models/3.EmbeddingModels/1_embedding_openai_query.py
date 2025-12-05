from langchain_opeai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents=["Delhi is the capital of India",
           "Bengaluru is the capital of karnataka",
           "Paris is the capital of France"]

result=embedding.embed_query("whats the capital city of karnataka")

print(str(result))




# from google import genai
# from google.genai.types import EmbedContentConfig
# from dotenv import load_dotenv
# import os

# load_dotenv()



# client = genai.Client()

# response = client.models.embed_content(
#     model="gemini-embedding-001",
#     contents=["whats the capital city of karnataka"],
#     config=EmbedContentConfig(
#         output_dimensionality=32  # or 3072 / 1536 / 768 as supported
#     )
# )

# embeddings = response.embeddings  # List containing one embedding vector
# print(str(embeddings))
