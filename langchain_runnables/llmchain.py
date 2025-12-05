from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template="suggest a catchy blog title about {topic}.",
    input_variables=["topic"]
)

chain=prompt | model

topic=input("Enter a topic")
output=chain.invoke(topic)

print("generated blog title:",output)