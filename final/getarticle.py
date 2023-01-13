import requests
import json

def get_article_links(company_name):



    # Extract the url links of the articles
    company_articles_links = []
    for article in articles['articles']:
        company_articles_links.append(article['url'])
    return company_articles_links