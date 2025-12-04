from flask import Blueprint, request, jsonify, current_app
from extensions import cache, db
from models import Article
import requests
import datetime

news_bp = Blueprint('news', __name__)

@news_bp.route('', methods=['GET'])
# @cache.cached(timeout=300, query_string=True)
def get_news():
    city = request.args.get('city')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    query = request.args.get('q')
    category = request.args.get('category')
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 20, type=int)

    api_key = current_app.config['NEWS_API_KEY']
    
    if api_key:
        # Fetch from external API
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'apiKey': api_key,
            'page': page,
            'pageSize': page_size
        }
        
        if query:
            url = 'https://newsapi.org/v2/everything'
            params['q'] = query
        elif category:
             params['category'] = category
             params['country'] = 'us' # Default to US if category is present but no query
        elif city:
            params['q'] = city
        elif lat and lon:
            # NewsAPI doesn't support lat/lon directly, so we might need to reverse geocode or just use a general query
            # For now, let's just query for "local" or similar if we had a way to map lat/lon to a place.
            # Since we don't have a geocoder here, we might skip this or use a mock.
            # A real app would reverse geocode lat/lon to a city name.
            pass
        else:
            params['country'] = 'us'

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            articles = []
            for item in data.get('articles', []):
                articles.append({
                    'external_id': item.get('url'), # Use URL as ID for now
                    'title': item.get('title'),
                    'description': item.get('description'),
                    'url': item.get('url'),
                    'source_name': item.get('source', {}).get('name'),
                    'published_at': item.get('publishedAt'),
                    'author': item.get('author'),
                    'content': item.get('content'),
                    'image_url': item.get('urlToImage'),
                    'location': city # Approximate
                })
            
            return jsonify({
                'articles': articles,
                'total_results': data.get('totalResults', 0)
            })

        except requests.RequestException as e:
            return jsonify({'error': 'Failed to fetch news', 'details': str(e)}), 500

    else:
        # Google News RSS Fallback (Real News)
        import feedparser
        import urllib.parse
        from bs4 import BeautifulSoup
        from geopy.geocoders import Nominatim
        
        base_url = 'https://news.google.com/rss'
        
        # Reverse geocoding if lat/lon provided but no city
        if lat and lon and not city:
            try:
                geolocator = Nominatim(user_agent="localnews_app")
                location = geolocator.reverse(f"{lat}, {lon}")
                if location and 'address' in location.raw:
                    city = location.raw['address'].get('city') or location.raw['address'].get('town') or location.raw['address'].get('village')
                    print(f"DEBUG: Resolved city from coordinates: {city}")
            except Exception as e:
                print(f"DEBUG: Geocoding failed: {e}")

        if query:
            rss_url = f'{base_url}/search?q={urllib.parse.quote(query)}&hl=en-US&gl=US&ceid=US:en'
        elif city:
            # Use 'loc:' operator for better local news targeting
            rss_url = f'{base_url}/search?q=loc:{urllib.parse.quote(city)}&hl=en-US&gl=US&ceid=US:en'
        elif lat and lon:
             # Fallback if geocoding failed
            rss_url = f'{base_url}/search?q=Local+News&hl=en-US&gl=US&ceid=US:en'
        elif category:
             rss_url = f'{base_url}/search?q={urllib.parse.quote(category)}&hl=en-US&gl=US&ceid=US:en'
        else:
            rss_url = f'{base_url}?hl=en-US&gl=US&ceid=US:en'

        print(f"DEBUG: RSS URL: {rss_url}")
        
        try:
            response = requests.get(rss_url, timeout=10)
            response.raise_for_status()
            feed = feedparser.parse(response.content)
        except requests.RequestException as e:
            print(f"DEBUG: Requests failed: {e}")
            return jsonify({'error': 'Failed to fetch news', 'details': str(e)}), 500

        articles = []
        start = (page - 1) * page_size
        end = start + page_size
        
        for entry in feed.entries[start:end]:
            image_url = None
            if 'media_content' in entry:
                image_url = entry.media_content[0]['url']
            elif 'media_thumbnail' in entry:
                image_url = entry.media_thumbnail[0]['url']
            
            title = entry.title
            source_name = "Google News"
            if ' - ' in title:
                parts = title.rsplit(' - ', 1)
                title = parts[0]
                source_name = parts[1]

            # Clean HTML from description
            description = ''
            if 'summary' in entry:
                soup = BeautifulSoup(entry.summary, 'html.parser')
                description = soup.get_text(separator=' ', strip=True)

            articles.append({
                'external_id': entry.link,
                'title': title,
                'description': description,
                'url': entry.link,
                'source_name': entry.source.title if 'source' in entry else source_name,
                'published_at': entry.published if 'published' in entry else datetime.datetime.utcnow().isoformat(),
                'author': entry.author if 'author' in entry else None,
                'content': description,
                'image_url': image_url,
                'location': city
            })
        
        return jsonify({
            'articles': articles,
            'total_results': len(feed.entries)
        })

@news_bp.route('/<path:external_id>', methods=['GET'])
@cache.cached(timeout=600)
def get_article_detail(external_id):
    # In a real app, we might fetch full content if not available in list
    # For now, we just return what we have or a mock
    return jsonify({
        'external_id': external_id,
        'title': 'Detailed Article View',
        'content': 'Full content would go here...'
    })
