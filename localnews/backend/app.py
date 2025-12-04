from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from extensions import db, migrate, jwt, cache

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cache.init_app(app)
    CORS(app)

    # Register blueprints
    from api.news import news_bp
    from api.auth import auth_bp
    from api.user import user_bp

    app.register_blueprint(news_bp, url_prefix='/news')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')

    @app.route('/')
    def index():
        return jsonify({"message": "LocalNews API is running"})

    return app
