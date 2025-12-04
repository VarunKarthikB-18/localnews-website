import pytest
from app import create_app
from extensions import db
from models import User, Article

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_register_login(client):
    # Register
    response = client.post('/auth/register', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201

    # Login
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_get_news(client):
    response = client.get('/news?city=New York')
    assert response.status_code == 200
    assert 'articles' in response.json

def test_save_article(client):
    # Register & Login
    client.post('/auth/register', json={'email': 'u@ex.com', 'password': 'pw'})
    login_res = client.post('/auth/login', json={'email': 'u@ex.com', 'password': 'pw'})
    token = login_res.json['access_token']
    headers = {'Authorization': f'Bearer {token}'}

    # Save article
    article_data = {
        'external_id': 'test-1',
        'title': 'Test Article',
        'url': 'http://example.com',
        'source_name': 'Test Source'
    }
    response = client.post('/user/saved-articles', json=article_data, headers=headers)
    if response.status_code != 201:
        print(response.json)
    assert response.status_code == 201

    # List saved
    response = client.get('/user/saved-articles', headers=headers)
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['article']['title'] == 'Test Article'
