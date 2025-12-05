from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path=r'C:\Users\sudha\OneDrive\Desktop\My_workspace\genai-Sudhanva\langchian_document_loaders\Social_Network_Ads.csv')

docs=loader.load()
print(len(docs))