from flask import Blueprint, request, jsonify
from extensions import db
from models import User, Article, SavedArticle
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify(user.to_dict()), 200

@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    data = request.get_json()
    
    if 'preferred_location' in data:
        user.preferred_location = data['preferred_location']
    
    if 'preferences' in data:
        user.set_preferences(data['preferences'])
        
    db.session.commit()
    return jsonify(user.to_dict()), 200

@user_bp.route('/saved-articles', methods=['POST'])
@jwt_required()
def save_article():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    external_id = data.get('external_id')
    if not external_id:
        return jsonify({"msg": "Missing external_id"}), 400

    # Check if article exists in DB, if not create it
    article = Article.query.filter_by(external_id=external_id).first()
    if not article:
        article = Article(
            external_id=external_id,
            title=data.get('title'),
            description=data.get('description'),
            url=data.get('url'),
            source_name=data.get('source_name'),
            published_at=None, # Parse if needed
            author=data.get('author'),
            content=data.get('content'),
            image_url=data.get('image_url'),
            location=data.get('location')
        )
        db.session.add(article)
        db.session.commit()
    
    # Check if already saved
    if SavedArticle.query.filter_by(user_id=current_user_id, article_id=article.id).first():
        return jsonify({"msg": "Article already saved"}), 400
        
    saved_article = SavedArticle(user_id=current_user_id, article_id=article.id, notes=data.get('notes'))
    article.saved_count += 1
    
    db.session.add(saved_article)
    db.session.commit()
    
    return jsonify({"msg": "Article saved"}), 201

@user_bp.route('/saved-articles', methods=['GET'])
@jwt_required()
def get_saved_articles():
    current_user_id = get_jwt_identity()
    saved = SavedArticle.query.filter_by(user_id=current_user_id).all()
    return jsonify([s.to_dict() for s in saved]), 200

@user_bp.route('/saved-articles/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_saved_article(id):
    current_user_id = get_jwt_identity()
    saved = SavedArticle.query.filter_by(id=id, user_id=current_user_id).first()
    
    if not saved:
        return jsonify({"msg": "Not found"}), 404
        
    db.session.delete(saved)
    db.session.commit()
    return jsonify({"msg": "Deleted"}), 200
