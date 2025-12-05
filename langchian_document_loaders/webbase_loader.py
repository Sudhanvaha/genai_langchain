from langchain_community.document_loaders import WebBaseLoader
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
    template="Answer the following question \n {question} from the following text - \n {text}",

    input_variables=['question','test']
)

parser=StrOutputParser()




url="https://www.flipkart.com/joker-witch-natalie-black-dial-rosegold-watch-analog-women/p/itmb4fb4ceeb6b8a?pid=WATGFAPKPAPQYQMH&lid=LSTWATGFAPKPAPQYQMH4OY521&marketplace=FLIPKART&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3AWATGFAHMGZ4RCEW8%3Bl%3ALSTWATGFAHMGZ4RCEW8JDWLQA%3Bpt%3App%3Buid%3A37a30225-62f3-11f0-9802-aff9835b52fc%3B.WATGFAPKPAPQYQMH&ppt=pp&ppn=pp&ssid=plop5f4wa80000001752745652437&otracker=pp_reco_Similar%2BProducts_4_34.productCard.PMU_HORIZONTAL_Joker%2B%2526%2BWitch%2BJoker%2Band%2BWitch%2BNatalie%2BBlack%2BDial%2BRosegold%2BWatch%2BAnalog%2BWatch%2B%2B-%2BFor%2BWomen_WATGFAPKPAPQYQMH_productRecommendation%2Fsimilar_3&otracker1=pp_reco_PINNED_productRecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_4_NA_view-all&cid=WATGFAPKPAPQYQMH&affExtParam1=fAzexCAbx5uiUCtvfvBiX4_p20397704&affid=atgwish&affExtParam2=4b7f871c66be5ac7630c27bb5e21fe7f"
loader=WebBaseLoader(url)

docs=loader.load()

chain=prompt | model | parser
print(chain.invoke({'question':'what is the price of the mentioned product','text':docs[0].page_content}))