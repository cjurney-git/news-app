import requests
from django.conf import settings
from news.models import Article

def fetch_news_articles():
    url = f"https://api.thenewsapi.com/v1/news/top?api_token={settings.api_key}&locale=us&limit=3"
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
        print(f"Article saved: {article_instance.title}")

def fetch_and_save_articles():
    articles = fetch_news_articles()
    save_articles_to_db(articles, Article) 
    return articles

# cron function to be run
def handleFetch():
    fetch_and_save_articles()