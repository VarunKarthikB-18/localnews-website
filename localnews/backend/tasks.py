from extensions import make_celery
from app import create_app
import os

app = create_app()
celery = make_celery(app)

@celery.task
def send_daily_digest():
    # Logic to fetch users with preferences and send email
    # For now, just log it
    print("Sending daily digest to users...")
    pass

@celery.task
def fetch_top_news_for_cities():
    # Logic to pre-fetch news for popular cities
    print("Fetching top news for major cities...")
    pass
