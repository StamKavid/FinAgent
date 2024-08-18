from langchain_openai import ChatOpenAI, AzureChatOpenAI
import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_base = os.getenv("OPENAI_API_BASE")

os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# # Local LLMs
# llm_llama = ChatOpenAI(
#     model = "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
#     base_url=os.getenv("OPENAI_API_BASE"),
#     api_key=os.getenv("OPENAI_API_KEY"),
#     temperature= 0.4
# )

# llm_gemma2 = ChatOpenAI(
#     model = "bartowski/gemma-2-9b-it-GGUF",
#     base_url=os.getenv("OPENAI_API_BASE"),
#     api_key=os.getenv("OPENAI_API_KEY"),
#     temperature= 0.4
# )

# Azure LLMs
llm_gpt35 = AzureChatOpenAI(
    openai_api_version="2024-02-01",
    azure_deployment="gpt-35-turbo",
)

llm_gpt4o = AzureChatOpenAI(
    openai_api_version="2024-02-01",
    azure_deployment="gpt-4o",
)