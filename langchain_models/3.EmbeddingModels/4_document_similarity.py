# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity 
# import numpy as np

# embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

# document =[
#     "Virat Kohli is an Indian cric eter known or is aggressive batting and leadership." ,
# "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
# "Sachin Tendulkar, also known as the 'God of Cricket' ,holds many batting records.",
# "Rohit Sharma is known for his elegant batting and record-breaking double centuries. " ,
# "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers. "
# ]

# query="tell me about virat kohli"

# doc_embeddings=embedding.embed_documents(documents)
# query_embeddings=embedding.embed_query(query)

# print(cosine_similarity([doc_embeddings],query_embeddings))#both should be 2d list



from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity 
embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
document =[
    "Virat Kohli is an Indian cric eter known or is aggressive batting and leadership." ,
"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
"Sachin Tendulkar, also known as the 'God of Cricket' ,holds many batting records.",
"Rohit Sharma is known for his elegant batting and record-breaking double centuries. " ,
"Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers. "
]

query="tell me about bumrah"

doc_embeddings=embedding.embed_documents(document)
query_embeddings=embedding.embed_query(query)

scores=cosine_similarity([query_embeddings],doc_embeddings)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(document[index])
print("similarity score is :",score)