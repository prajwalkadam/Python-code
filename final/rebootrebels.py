import requests
import json
from newsapi import NewsApiClient
from textblob import TextBlob

api_key = '2819a8a3246744769031ea1906167559'

'''
source:id,name
author
title
description
url
urlToImage
publishedAt
content
'''
def call_api(company_name):
    url = f'https://newsapi.org/v2/everything?q={company_name}&sortBy=relevancy&apiKey={api_key}'
    response = requests.get(url)

    # Parse the JSON data
    articles = json.loads(response.text)
    return articles


def get_article_links(articles):
    # Extract the url links of the articles
    company_articles_links = []
    for article in articles['articles']:
        company_articles_links.append(article['url'])

    return company_articles_links

def reputational_threat_links(articles):
    threat_articles_links = []
    for article in articles['articles']:
        text = article['title'] + ' ' + article['content']
        sentiment = TextBlob(text)
        if sentiment.sentiment.polarity < -0.2:
            threat_articles_links.append(article['url'])
    return threat_articles_links

def reputational_threat_articles(articles):
    threat_articles_articles = []
    for article in articles['articles']:
        text = article['title'] + ' ' + article['content']
        sentiment = TextBlob(text)
        if sentiment.sentiment.polarity < -0.2:
            threat_articles_articles.append(article)
    # return the list of reputationalthreatening articles
    return threat_articles_articles

def reputational_threat_sentences(articles):
    articles=reputational_threat_articles(articles)
    reputational_threat_sentences=[]
    if len(articles) > 0:
        for article in articles:
            # print(f"{article['title']} - {article['description']}")
            reputational_threat_sentences.append(f"{article['title']} - {article['description']}")
    # else:
        # print(f"No reputational threatening articles were found.")
    return reputational_threat_sentences
