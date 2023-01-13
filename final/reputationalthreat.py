import requests
from newsapi import NewsApiClient
import json
from newsapi import NewsApiClient
from textblob import TextBlob
def reputational_threat(company_name):
    # Initialize the NewsAPI client with your API key
    # newsapi = NewsApiClient(api_key='2819a8a3246744769031ea1906167559')
    #
    # # Search for articles containing the company name and keywords related to the company's reputation
    # articles = newsapi.get_everything(
    #     q=company_name + ' AND (scandal OR lawsuit OR fraud OR bankruptcy OR corruption OR layoff OR sueing)',
    #     language='en')
    api_key='2819a8a3246744769031ea1906167559'

    url = f'https://newsapi.org/v2/everything?q={company_name}&sortBy=relevancy&apiKey={api_key}'
    response = requests.get(url)

    # Parse the JSON data
    articles = json.loads(response.text)
    # perform sentiment analysis on the articles
    threat_articles = []
    for article in articles['articles']:
        text = article['title'] + ' ' + article['content']
        sentiment = TextBlob(text)
        if sentiment.sentiment.polarity < -0.2:
            threat_articles.append(article)
    # return the list of reputationalthreatening articles
    return threat_articles