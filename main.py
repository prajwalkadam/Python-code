#
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # import json
# # # # # from newsapi import NewsApiClient
# # # # # from textblob import TextBlob
# # # # #
# # # # # def reputational_threat(company_name):
# # # # #     # Initialize the NewsAPI client with your API key
# # # # #     newsapi = NewsApiClient(api_key='2819a8a3246744769031ea1906167559')
# # # # #
# # # # #     # Search for articles containing the company name and keywords related to the company's reputation
# # # # #     articles = newsapi.get_everything(q=company_name + ' AND (scandal OR lawsuit OR fraud OR bankruptcy OR corruption)', language='en')
# # # # #     # perform sentiment analysis on the articles
# # # # #     threat_articles = []
# # # # #     for article in articles['articles']:
# # # # #         text = article['title'] + ' ' + article['description']
# # # # #         sentiment = TextBlob(text)
# # # # #         if sentiment.sentiment.polarity < -0.2:
# # # # #             threat_articles.append({"url": article["url"], "title": article["title"], "description": article["description"]})
# # # # #     # return the list of reputationalthreatening articles
# # # # #     return threat_articles
# # # # #
# # # # # # Usage
# # # # # print("Enter company name :")
# # # # # company_name = input()
# # # # # articles = reputational_threat(company_name)
# # # # # if len(articles) > 0:
# # # # #     print(f"Reputationalthreatening articles about {company_name}")
# # # # #     for article in articles:
# # # # #         print(f"{article['title']} - {article['description']} - {article['url']}")
# # # # # else:
# # # # #     print(f"No reputationalthreatening articles about {company_name} were found.")
# # # #
# # # #
# # # #
# # # # import json
# # # # import os
# # # # from newsapi import NewsApiClient
# # # #
# # # # def download_articles(company_name):
# # # #     # Initialize the NewsAPI client with your API key
# # # #     newsapi = NewsApiClient(api_key='2819a8a3246744769031ea1906167559')
# # # #
# # # #     # Search for articles containing the company name in the title
# # # #     articles = newsapi.get_everything(q='title:' + company_name, language='en')
# # # #
# # # #     # Create a directory to store the articles
# # # #     if not os.path.exists(company_name):
# # # #         os.makedirs(company_name)
# # # #
# # # #     # Download and save each article
# # # #     for article in articles['articles']:
# # # #         with open(f"{company_name}/{article['title']}.txt", "w") as file:
# # # #             file.write(json.dumps(article))
# # # #     print(f"{len(articles['articles'])} articles about {company_name} have been downloaded and saved.")
# # # #
# # # # # Usage
# # # # print("Enter company name :")
# # # # company_name = input()
# # # # download_articles(company_name)
# #
# # #
# import os
# import requests
# import json
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
#
# # Your NewsAPI key
# api_key = '2819a8a3246744769031ea1906167559'
#
# # The name of the company to search for in article titles
# print("Enter company name: ")
# company_name = input()
#
# # Make the GET request to the NewsAPI
# url = f'https://newsapi.org/v2/everything?q={company_name}&sortBy=relevancy&apiKey={api_key}'
# response = requests.get(url)
#
# # Parse the JSON data
# data = json.loads(response.text)
#
# # Print the URLs of the articles
# for article in data['articles']:
#     print(article['url'])
#     directory = 'articles'
#
#     # Create the directory if it does not exist
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     # Make the GET request to the NewsAPI
#     url = f'https://newsapi.org/v2/everything?q={company_name}&sortBy=relevancy&apiKey={api_key}'
#     response = requests.get(url)
#
#     # Parse the JSON data
#     data = json.loads(response.text)
#
#     # Download the articles and save them to the specified directory
#     # count=0
#     # for article in data['articles']:
#     #     url = article['url']
#     #     title = article['title']
#     #     response = requests.get(url)
#     #     try:
#     #         count+=1
#     #         with open(f'{directory}/{count}.html', 'w', encoding="utf-8", errors='ignore') as f:
#     #             f.write(response.text)
#     #     except:
#     #         print("An exception occurred for " + f'{directory}/{title}.html')
#
# # Initialize the sentiment analyzer
# sia = SentimentIntensityAnalyzer()
#
# # List to store the potentially threatening data
# threatening_data = []
#
# # Analyze the articles and print any potentially threatening data
# for article in os.listdir(directory):
#     with open(f'{directory}/{article}', 'r') as f:
#         text = f.read()
#         # Use the sentiment analyzer to get the compound score of the text
#         score = sia.polarity_scores(text)['compound']
#         if score < -0.5: # set threshold for the compound score
#             threatening_data.append(text)
#
# if len(threatening_data)>0:
#     print("Potentially Reputation Threatening Data:")
#     for threat in threatening_data:
#         print(threat)
# else:
#     print("No Reputation Threatening Data Found!")