from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
    
)
model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

prompt2=PromptTemplate(
    template="explain about this joke /n{text}",
    input_variables=["text"]
)

chain=RunnableSequence(prompt1 ,model,parser,prompt2,model,parser)
result=chain.invoke({'topic':"cricket"})
print(result)