# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()


# st.header("Research tool")

# user_input=st.text_input("Enter your prompt")

# if st.button('Summarize):
#     st.text("Some random text")


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt


# Load environment variables (make sure you have GOOGLE_API_KEY in your .env file)
load_dotenv()

st.header("Research tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template=load_prompt('template.json')


#filling the placeholders
# prompt=template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input

# })


# Create Gemini model instance
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")



if st.button("Summarize"):
    chain=template | model
    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })
    st.write(result.content)
