from langchain_core.output_parsers import JsonOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
)
model= ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic')
]

parser=StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template='give 3 facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain= template | model | parser
result=chain.invoke({'topic':'cricket_game'})
# prompt=template.invoke({'topic':'cricket'})

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

print(result)