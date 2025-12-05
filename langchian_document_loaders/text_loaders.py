from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2-Exp',
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template="write a summary from the following poem - \n {poem}",
    input_variables=['poem']
)

parser=StrOutputParser()

loader=TextLoader(r'C:\Users\sudha\OneDrive\Desktop\My_workspace\genai-Sudhanva\langchian_document_loaders\cricket.txt',encoding='utf-8')

docs=loader.load()

# print(type(docs))
# print(len(docs))
# print(type(docs[0]))

# print(docs[0].metadata)

chain=prompt | model | parser
print(chain.invoke({'poem':docs[0].page_content}))