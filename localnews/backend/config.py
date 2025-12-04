import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///localnews.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    # Caching
    CACHE_TYPE = os.environ.get('CACHE_TYPE') or 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
    if os.environ.get('REDIS_URL'):
        CACHE_REDIS_URL = os.environ.get('REDIS_URL')

    # Celery
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
