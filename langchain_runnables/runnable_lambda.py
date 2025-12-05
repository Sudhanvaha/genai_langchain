from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda
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

joke_gen=RunnableSequence(prompt1 ,model,parser)

# prompt2=PromptTemplate(
#     template="explain about this joke /n{text}",
#     input_variables=["text"]
# )



parallel_chain=RunnableParallel(
    {
        'words':RunnableLambda(lambda x: len(x.split())),
        'joke':RunnablePassthrough()
    }
)

final_chain=RunnableSequence(joke_gen,parallel_chain)
result=final_chain.invoke({'topic':'cricket'})

final_result="""{} \n word count - {}""".format(result['joke'],result['words'])
print(final_result)  