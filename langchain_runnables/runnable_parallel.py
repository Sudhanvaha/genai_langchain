from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI



llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
# model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

prompt1=PromptTemplate(
    template="generate a tweet on this {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="generate a linkedin post on this {topic}",
    input_variables=['topic']
)
parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin': RunnableSequence(prompt2,model,parser)
})
result=parallel_chain.invoke({'topic':'AI'})
print(result)