import json
import os

import requests
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


class SearchTools():
  @tool("Search the internet")
  def search_internet(query):
    """Useful to search the internet 
    about a a given topic and return relevant results"""
    top_result_to_return = 4
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    return '\n'.join(string)

  @tool("Search the internet via DuckDuckGo API")
  def search_internet_duck(query):
    """Useful to search the internet 
    about a a given topic and return relevant results based on DuckDuckGo API"""
    time = "d"
    max_results = 5
    wrapper = DuckDuckGoSearchAPIWrapper(time= time, max_results=max_results)
    search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")

    return search.run(query)

  @tool("Search news on the internet")
  def search_news(query):
    """Useful to search news about a company, stock, cryptocurrency or any other
    topic and return relevant results"""""
    top_result_to_return = 4
    url = "https://google.serper.dev/news"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['news']
    string = []
    for result in results[:top_result_to_return]:
      try:
        string.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    return '\n'.join(string)