from crewai import Task
from textwrap import dedent

class CryptoAnalysisTasks():
  def research(self, agent, crypto):
    return Task(
        description=dedent(f"""
            Collect and summarize recent news articles, press releases, and market analyses 
            related to the cryptocurrency {crypto} and its industry. Pay special attention 
            to any significant events, market sentiments, analysts' opinions, and upcoming 
            events such as earnings reports.

            Your final answer MUST be a comprehensive report that includes:
            - A detailed summary of the latest news
            - Any notable shifts in market sentiment
            - Potential impacts on {crypto}
            - The cryptocurrency ticker: {crypto}

            Ensure to use the most recent data available. 
            {self.__tip_section()}
        """),
        agent=agent,
        expected_output=dedent("""
            A comprehensive report that includes:
            - A detailed summary of the latest news
            - Any notable shifts in market sentiment
            - Potential impacts on the cryptocurrency
            - The cryptocurrency ticker
        """)
    )
    
  def financial_analysis(self, agent):
    return Task(
        description=dedent(f"""
            Conduct a thorough analysis of the cryptocurrency's financial health and market performance. 
            This includes examining key financial metrics such as:
            - 24-hour trading volume
            - Circulating supply
            - Market capitalization
            - Total value locked (TVL)

            Additionally, analyze the cryptocurrency's performance in comparison to its peers and overall market trends.

            Your final report MUST include:
            - An expanded summary of the analysis
            - A clear assessment of the cryptocurrency's financial standing
            - Its strengths and weaknesses
            - A comparison with its competitors in the current market scenario

            Ensure to use the most recent data available.
            {self.__tip_section()}
        """),
        agent=agent,
        expected_output=dedent("""
            A detailed report that includes:
            - An expanded summary of the analysis
            - A clear assessment of the cryptocurrency's financial standing
            - Its strengths and weaknesses
            - A comparison with its competitors in the current market scenario
        """)
    )

  def recommend(self, agent):
    return Task(
        description=dedent(f"""
            Review and synthesize the analyses provided by the Financial Analyst and the Research Analyst. 
            Combine these insights to form a comprehensive investment recommendation.

            You MUST consider all aspects, including:
            - Financial health
            - Market sentiment
            - Insider trading activity
            - Upcoming events

            Your final report MUST include:
            - Whether the market is bullish, bearish, or neutral for the specific crypto.
            - A detailed and clear investment stance and strategy
            - Supporting evidence from the analyses
            - Well-formatted sections for readability and presentation

            Ensure the report is comprehensive, professional, and aesthetically pleasing for your customer.
            {self.__tip_section()}
        """),
        agent=agent,
        expected_output=dedent("""
            A comprehensive investment recommendation report for the next week that includes:
            - A clear investment stance and strategy
            - Whether the market is bullish, bearish, or neutral for the specific crypto.
            - Supporting evidence from financial and market analyses
            - Sections on insider trading activity and upcoming events
            - Professional and well-formatted presentation
        """)
    )

  def __tip_section(self):
    return "Deliver your BEST WORK and earn a $10,000 commission!"