import requests
from django.conf import settings
from news.models import Article
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env
api_key = os.getenv('API_KEY')

def fetch_news_articles():
    url = f"https://api.thenewsapi.com/v1/news/top?api_token={api_key}&locale=us&language=en&limit=3"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        return []

def save_articles_to_db(articles, ArticleModel):
    for article in articles:
        article_instance = ArticleModel(
            uuid=article["uuid"],
            title=article["title"],
            description=article["description"],
            keywords=article["keywords"],
            snippet=article["snippet"],
            published_date=article["published_at"],
            source=article["source"],
            image_url=article["image_url"],
            url=article["url"],
            language=article["language"],
            categories=article["categories"],
            locale=article["locale"]
        )
        article_instance.save()
        print(f"Article saved: {article_instance.title}")

def fetch_and_save_articles():
    articles = fetch_news_articles()
    save_articles_to_db(articles, Article) 
    return articles

# cron function to be run
def handleFetch():
    fetch_and_save_articles()