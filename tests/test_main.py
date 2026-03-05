# tests/test_main.py

import pytest
from flask.testing import FlaskClient
from src.main import app
import os
import webbrowser

# Setup and teardown
@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client

# Happy path tests
def test_index_page_returns_200(client: FlaskClient):
    # Verify that the index page returns a 200 status code
    response = client.get('/')
    assert response.status_code == 200

def test_index_page_returns_html(client: FlaskClient):
    # Verify that the index page returns HTML content
    response = client.get('/')
    assert 'text/html' in response.content_type

# Edge cases tests
def test_index_page_with_empty_query_string(client: FlaskClient):
    # Verify that the index page returns a 200 status code with an empty query string
    response = client.get('/?')
    assert response.status_code == 200

def test_index_page_with_none_query_string(client: FlaskClient):
    # Verify that the index page returns a 200 status code with a None query string
    response = client.get('/')
    assert response.status_code == 200

# Error cases tests
def test_index_page_with_invalid_path(client: FlaskClient):
    # Verify that an invalid path returns a 404 status code
    response = client.get('/invalid-path')
    assert response.status_code == 404

def test_index_page_with_invalid_method(client: FlaskClient):
    # Verify that an invalid HTTP method returns a 405 status code
    response = client.post('/')
    assert response.status_code == 405

# Security cases tests
def test_index_page_with_malformed_data(client: FlaskClient):
    # Verify that the index page returns a 400 status code with malformed data
    response = client.get('/<script>alert("XSS")</script>')
    assert response.status_code == 400

# Integration tests
def test_app_runs_without_errors():
    # Verify that the app runs without errors
    app.run(debug=False)

def test_index_html_file_exists():
    # Verify that the index.html file exists
    assert os.path.exists('templates/index.html')

def test_webbrowser_module_imports():
    # Verify that the webbrowser module imports without errors
    import webbrowser

# Test for app instance
def test_app_instance():
    # Verify that the app instance is created
    assert isinstance(app, Flask)

# Test for route registration
def test_route_registration():
    # Verify that the route is registered
    assert '/' in app.url_map._rules

# Test for template rendering
def test_template_rendering(client: FlaskClient):
    # Verify that the template is rendered correctly
    response = client.get('/')
    assert b'index.html' in response.data