from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path=r"C:\Users\sudha\OneDrive\Desktop\My_workspace\genai-Sudhanva\langchian_document_loaders\books",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load()

for documnet in docs:
    print(documnet.metadata)