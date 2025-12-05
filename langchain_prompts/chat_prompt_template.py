from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} expert'),
    ('human','explain in simple terms {topic}')


    # SystemMessage(content='you are a helpful {domain} expert'),
    # HumanMessage(content='explain in simple terms {topic}') doesnot work in chat_prompt_template
])

prompt=chat_template.invoke({'domain':'cricket','topic':'googly'})

print(prompt)