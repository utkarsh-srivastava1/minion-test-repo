# tests/test_user.py
import pytest
from flask.testing import FlaskClient
from src.user import app, RegistrationForm, csrf
import bcrypt
import json

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_happy_path(client: FlaskClient):
    # Verify that a valid registration request returns a 201 status code
    form = RegistrationForm(username='testuser', password='testpassword')
    with client:
        response = client.post('/register', data={'username': 'testuser', 'password': 'testpassword', 'csrf_token': generate_csrf()})
        assert response.status_code == 201
        assert json.loads(response.data)['message'] == 'User created successfully'

def test_empty_username(client: FlaskClient):
    # Verify that an empty username returns a 400 status code
    with client:
        response = client.post('/register', data={'username': '', 'password': 'testpassword', 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_empty_password(client: FlaskClient):
    # Verify that an empty password returns a 400 status code
    with client:
        response = client.post('/register', data={'username': 'testuser', 'password': '', 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_short_username(client: FlaskClient):
    # Verify that a username shorter than 4 characters returns a 400 status code
    with client:
        response = client.post('/register', data={'username': 'abc', 'password': 'testpassword', 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_long_username(client: FlaskClient):
    # Verify that a username longer than 15 characters returns a 400 status code
    with client:
        response = client.post('/register', data={'username': 'a' * 16, 'password': 'testpassword', 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_short_password(client: FlaskClient):
    # Verify that a password shorter than 8 characters returns a 400 status code
    with client:
        response = client.post('/register', data={'username': 'testuser', 'password': 'abc', 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_long_password(client: FlaskClient):
    # Verify that a password longer than 80 characters returns a 400 status code
    with client:
        response = client.post('/register', data={'username': 'testuser', 'password': 'a' * 81, 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_null_username(client: FlaskClient):
    # Verify that a null username returns a 400 status code
    with client:
        response = client.post('/register', data={'username': None, 'password': 'testpassword', 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_null_password(client: FlaskClient):
    # Verify that a null password returns a 400 status code
    with client:
        response = client.post('/register', data={'username': 'testuser', 'password': None, 'csrf_token': generate_csrf()})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_invalid_csrf_token(client: FlaskClient):
    # Verify that an invalid CSRF token returns a 400 status code
    with client:
        response = client.post('/register', data={'username': 'testuser', 'password': 'testpassword', 'csrf_token': 'invalid'})
        assert response.status_code == 400
        assert json.loads(response.data)['message'] == 'Invalid request'

def test_password_hashing():
    # Verify that the password hashing function works correctly
    password = 'testpassword'
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    assert bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def test_password_hashing_collision():
    # Verify that the password hashing function does not produce collisions
    password1 = 'testpassword1'
    password2 = 'testpassword2'
    hashed_password1 = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    hashed_password2 = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
    assert hashed_password1 != hashed_password2

def test_csrf_token_generation():
    # Verify that the CSRF token generation function works correctly
    token = generate_csrf()
    assert token is not None

def test_csrf_token_validation(client: FlaskClient):
    # Verify that the CSRF token validation function works correctly
    with client:
        response = client.post('/register', data={'username': 'testuser', 'password': 'testpassword', 'csrf_token': generate_csrf()})
        assert response.status_code == 201
        assert json.loads(response.data)['message'] == 'User created successfully'