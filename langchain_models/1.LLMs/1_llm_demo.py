# from langchain_openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm=OpenAI(model='gpt-3.5-turbo-instruct')

# result=llm.invoke("what is the capital city of India")

# print(result)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini LLM (you can use gemini-1.5-flash or gemini-1.5-pro)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Invoke the model with a simple query
result = llm.invoke("What is the capital city of India?")

print(result.content)

