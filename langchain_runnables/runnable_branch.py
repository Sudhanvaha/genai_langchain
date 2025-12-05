from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableBranch,RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Summarize the following text\n {text}",
    input_variables=["text"]
)
llm1=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
)
model1=ChatHuggingFace(llm=llm1)

# llm2=HuggingFaceEndpoint(
#     repo_id='inclusionAI/Ring-1T-preview',
#     task="text-generation"
# )
# model2=ChatHuggingFace(llm=llm2)

parser=StrOutputParser()

report_gen=RunnableSequence(prompt1,model1,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>300,RunnableSequence(prompt2,model1,parser)),
    RunnablePassthrough()

)


final_chain=RunnableSequence(report_gen,branch_chain)

print(final_chain.invoke({'topic':'Russian'}))