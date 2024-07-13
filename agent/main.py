from crewai import Crew
from textwrap import dedent

from crypto_analysis_agents import CryptoAnalysisAgents
from crypto_analysis_tasks import CryptoAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class FinancialCrew:
  def __init__(self, crypto):
    self.crypto = crypto

  def run(self):
    agents = CryptoAnalysisAgents()
    tasks = CryptoAnalysisTasks()

    research_analyst_agent = agents.research_analyst()
    financial_analyst_agent = agents.financial_analyst()
    investment_advisor_agent = agents.investment_advisor()

    research_task = tasks.research(research_analyst_agent, self.crypto)
    financial_task = tasks.financial_analysis(financial_analyst_agent)
    recommend_task = tasks.recommend(investment_advisor_agent)

    crew = Crew(
      agents=[
        research_analyst_agent,
        financial_analyst_agent,
        investment_advisor_agent
      ],
      tasks=[
        research_task,
        financial_task,
        recommend_task
      ],
      verbose=True,
      output_log_file = "financial_analysis_crew.log"
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  crypto = input(
    dedent("""
      What is the crypto you want to analyze?
    """))
  
  financial_crew = FinancialCrew(crypto)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)