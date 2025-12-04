from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import json

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    preferred_location = db.Column(db.String(100))
    preferences = db.Column(db.Text, default='{}') # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    saved_articles = db.relationship('SavedArticle', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_preferences(self):
        try:
            return json.loads(self.preferences)
        except:
            return {}

    def set_preferences(self, prefs):
        self.preferences = json.dumps(prefs)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'preferred_location': self.preferred_location,
            'preferences': self.get_preferences(),
            'created_at': self.created_at.isoformat()
        }

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(255), unique=True) # ID from API or generated
    title = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String(500), nullable=False)
    source_name = db.Column(db.String(100))
    published_at = db.Column(db.DateTime)
    author = db.Column(db.String(100))
    content = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    location = db.Column(db.String(100))
    saved_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'external_id': self.external_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'source_name': self.source_name,
            'published_at': self.published_at.isoformat() if self.published_at else None,
            'author': self.author,
            'content': self.content,
            'image_url': self.image_url,
            'location': self.location,
            'saved_count': self.saved_count
        }

class SavedArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    notes = db.Column(db.Text)
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)

    article = db.relationship('Article')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'article': self.article.to_dict(),
            'notes': self.notes,
            'saved_at': self.saved_at.isoformat()
        }
