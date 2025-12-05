# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model=ChatOpenAI(model='gpt-4')

# result=model.invoke("What is the capital of karnataka")   

# print(result)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini chat model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=1,max_completion_tokens=10)  
# temperature=0-0.7(deterministic or predictable task)
# >.5-1 (more creative for gemini) and for openai >.75-1.5

# You can also use "gemini-1.5-pro" for more complex reasoning

# Invoke the model
result = model.invoke("Write a 5 line poem on moder day gratest virat kohli")

print(result.content)
