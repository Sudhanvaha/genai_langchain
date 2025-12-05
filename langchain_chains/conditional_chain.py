from langchain_core.prompts import PromptTemplate
from  dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI
# model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")



llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['Positive','Negative']=Field(description="Give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction':parser2.get_format_instructions}
)

classifier_chain=prompt1 | model | parser2

# branch_chain=RunnableBranch(
#     (condition1,chain),
#     (condition2,chain),
#     default chain
# )


prompt2=PromptTemplate(
    template="write an appropriate single line response to this positive feedback\n {feedback}",
    input_variables=["feedback"]
)

prompt3=PromptTemplate(
    template="write an appropriate single line response to this negative feedback\n {feedback}",
    input_variables=["feedback"]
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="Positive",prompt2 | model | parser),
    (lambda x:x.sentiment=="Negative",prompt3 | model | parser),
    RunnableLambda(lambda x:"Could not find sentiment")
)

chain=classifier_chain | branch_chain

print(chain.invoke({'feedback':'This is an Awesome phone'}))

chain.get_graph().print_ascii()