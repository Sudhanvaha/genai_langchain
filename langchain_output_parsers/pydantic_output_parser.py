from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
)
model= ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name :str=Field(description='Name of the person'),
    age : int = Field(gt=18,description='Age of the person'),
    city : str = Field(description="Name of the city person belongs to ")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="generate a name,age ,city of the fictional {place} person\n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt=template.invoke({'place':'India'})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template | model | parser
final_result=chain.invoke({'place':'India'})
print(final_result)