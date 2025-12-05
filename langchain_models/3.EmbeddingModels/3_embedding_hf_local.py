from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Bengaluru is the capital of Karnataka",
    "Paris is the capital of France"
]

vector=embedding.embed_documents(documents)

print(str(vector))