"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
from app.utils.redis import REDIS_CLIENT


@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str


def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 
    articles = REDIS_CLIENT.get_entry("all_articles")
    return [format_article(article) for article in articles]


def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    # 2. Return as a list of articles sorted by most recent date
    articles = get_all_news
    return articles.sort(reverse=True, key= (lambda article: article.publish_date))

def format_article(data: dict) -> Article:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 
    return Article (
        author = data["author"],
        title = data["title"],
        body = data["text"],
        publish_date = datetime.fromisoformat(data["published"]),
        image_url = data["main_image"],
        url = data["URL"]    
    )
