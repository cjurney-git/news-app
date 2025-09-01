import requests
from django.conf import settings

import models
def fetch_news_articles():
    url = f"https://api.thenewsapi.com/v1/news/headlines?locale=us&language=en&api_token={settings.api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["articles"]
    else:
        return []

def save_articles_to_db(articles, ArticleModel):
    for article in articles:
        article_instance = ArticleModel(
            title=article["title"],
            content=article["content"],
            published_date=article["published_date"],
            source=article["source"],
            url=article["url"]
        )
        article_instance.save()

def fetch_and_save_articles():
    ArticleModel = models.Article
    articles = fetch_news_articles()
    save_articles_to_db(articles, ArticleModel)


