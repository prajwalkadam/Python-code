import spacy
import os

from nltk.sentiment import SentimentIntensityAnalyzer as sia

import rebootrebels as rr
import nltk

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the company name
company_name = "Google"

# List to store the potentially threatening data
threatening_data = []
articles = rr.call_api(company_name)


# Analyze the articles and print any potentiallythreatening data
for article in articles:
    # with open(f'{directory}/{article}', 'r') as f:

    # Use the NER module to extract entities from the text
    doc = nlp(article['content'])
    for ent in doc.ents:
        if ent.label_ == "ORG" and ent.text.lower() == company_name.lower():
            score = sia.polarity_scores(article)['compound']
            if score < -0.5:
                threatening_data.append(article)

if len(threatening_data) > 0:
    print("Potentially Reputation Threatening Data:")
    for threat in threatening_data:
        print(threat)
else:
    print("No Reputation Threatening Data Found!")
