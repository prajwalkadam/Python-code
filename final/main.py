import rebootrebels as rr

company_name = input()
art = rr.call_api(company_name)
# article_links=rr.get_article_links(art)
# for article in article_links:
#     print(article)
threat_links = rr.reputational_threat_links(art)
for link in threat_links:
    print(link)
sentences = rr.reputational_threat_sentences(art)
for sentence in sentences:
    print(sentence)