from app import create_app
from extensions import db
from models import User, Article
from werkzeug.security import generate_password_hash

app = create_app()

def seed():
    with app.app_context():
        print("Seeding data...")
        
        # Create test user
        if not User.query.filter_by(email='test@example.com').first():
            user = User(email='test@example.com', preferred_location='New York')
            user.set_password('password123')
            db.session.add(user)
            print("Created test user: test@example.com / password123")

        # Create some articles
        if Article.query.count() == 0:
            articles = [
                Article(
                    external_id='seed-1',
                    title='Local News: New Park Opens',
                    description='A new park has opened in the city center.',
                    url='https://example.com/news/park',
                    source_name='City Gazette',
                    location='New York',
                    content='Full content of the article...'
                ),
                Article(
                    external_id='seed-2',
                    title='Tech Trends 2025',
                    description='What to expect in the tech world next year.',
                    url='https://example.com/news/tech',
                    source_name='Tech Daily',
                    location='San Francisco',
                    content='Full content of the article...'
                )
            ]
            db.session.add_all(articles)
            print(f"Created {len(articles)} seed articles")

        db.session.commit()
        print("Seeding complete.")

if __name__ == '__main__':
    seed()
