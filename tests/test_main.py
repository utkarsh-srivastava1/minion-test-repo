# tests/test_main.py

import pytest
from flask.testing import FlaskClient
from src.main import app
import os
import tempfile
import shutil

# Setup and teardown
@pytest.fixture
def client():
    # Create a temporary directory for the test
    temp_dir = tempfile.mkdtemp()
    # Save the current working directory
    cwd = os.getcwd()
    # Change the working directory to the temporary directory
    os.chdir(temp_dir)
    # Create a test client
    with app.test_client() as client:
        yield client
    # Change back to the original working directory
    os.chdir(cwd)
    # Remove the temporary directory
    shutil.rmtree(temp_dir)

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

def test_index_page_with_query_string(client: FlaskClient):
    # Verify that the index page returns a 200 status code with a query string
    response = client.get('/?test=query')
    assert response.status_code == 200

# Error cases tests
def test_index_page_with_invalid_path(client: FlaskClient):
    # Verify that an invalid path returns a 404 status code
    response = client.get('/invalid')
    assert response.status_code == 404

def test_index_page_with_invalid_method(client: FlaskClient):
    # Verify that an invalid method returns a 405 status code
    response = client.post('/')
    assert response.status_code == 405

# Security cases tests
def test_index_page_with_malformed_query_string(client: FlaskClient):
    # Verify that a malformed query string returns a 400 status code
    response = client.get('/?<script>alert("XSS")</script>')
    assert response.status_code == 400

def test_index_page_with_sql_injection(client: FlaskClient):
    # Verify that a SQL injection attempt returns a 400 status code
    response = client.get('/?id=1\' OR 1=1')
    assert response.status_code == 400

# Test that the app runs without errors
def test_app_runs_without_errors():
    # Verify that the app runs without errors
    app.run(debug=False)

# Test that the index.html template exists
def test_index_html_template_exists():
    # Verify that the index.html template exists
    assert os.path.exists('templates/index.html')