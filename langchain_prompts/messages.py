from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)