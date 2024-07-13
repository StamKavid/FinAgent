from crewai import Agent

from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from langchain_community.tools import YahooFinanceNewsTool
from langchain_openai import ChatOpenAI
import os
import openai
from textwrap import dedent
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

llm_llama = ChatOpenAI(
    model = "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature= 0.4
)

llm_gemma2 = ChatOpenAI(
    model = "bartowski/gemma-2-9b-it-GGUF",
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature= 0.4
)

class CryptoAnalysisAgents():
  def financial_analyst(self):
    return Agent(
      role='The Best Financial Analyst',
      goal= dedent("""
                  Impress all customers with your comprehensive financial data analysis,
                  market trends insights, and investment strategies tailored for the cryptocurrency market.
                   """),
      backstory= dedent("""
                  You are the most seasoned financial analyst with extensive expertise in 
                  cryptocurrency market analysis and investment strategies. Known for your 
                  impeccable track record and in-depth knowledge, technical analyses, 
                  you work for a super important customer who demands the highest level of precision and insight. 
                        """),
      verbose=True,
      tools=[
        SearchTools.search_internet,
        # SearchTools.search_internet_duck,
        CalculatorTools.calculate,
      ],
      llm = llm_gemma2
    )

  def research_analyst(self):
    return Agent(
      role='Staff Research Analyst',
      goal= dedent("""
                  Excel at gathering, interpreting, and presenting data to provide unparalleled 
                  insights and amaze your customers with your thorough and precise analysis.
                   """),
      backstory= dedent("""
                        Renowned as the BEST research analyst, you possess exceptional skills in sifting 
                        through news, company announcements, market sentiments and daily prices. Your expertise lies 
                        in transforming raw data into valuable insights. Currently, you are working for a 
                        high-profile client who relies on your analytical prowess to make informed decisions. 
                        Your ability to deliver accurate and relevant information sets you apart in the industry.
                        """),
      verbose=True,
      tools=[
        SearchTools.search_internet,
        SearchTools.search_news,
        YahooFinanceNewsTool(),
      ],
      llm = llm_gemma2
  )

  def investment_advisor(self):
    return Agent(
      role='Private Investment Advisor',
      goal= dedent( """
                    Provide your customers with comprehensive analyses of cryptocurrencies
                    and formulate strategic investment recommendations that are tailored to their needs.
                    Ensure your advice is data-driven, insightful, and actionable.
                    """),
      backstory= dedent("""
                        As the most experienced investment advisor, you excel at combining various analytical 
                        insights to formulate strategic investment advice. Your expertise spans across multiple 
                        financial domains, with a particular focus on cryptocurrencies. Currently, you are working 
                        for a high-profile client who expects nothing short of excellence. Your ability to deliver 
                        precise and impactful recommendations is crucial to impress and retain this important client.
                        """),
      verbose=True,
      tools=[
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
        YahooFinanceNewsTool()
      ],
      llm = llm_gemma2
    )