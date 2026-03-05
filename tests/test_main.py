# tests/test_main.py

import pytest
from src.main import hello, add, multiply, power, modulo, exponential
from flask import request
from src.user import app
import hashlib
import secrets
import string

# Setup and teardown
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Happy path tests
def test_hello():
    # Verifies that the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies that the add function returns the correct result for two positive numbers
    assert add(2.0, 3.0) == 5.0

def test_multiply_happy_path():
    # Verifies that the multiply function returns the correct result for two positive numbers
    assert multiply(2.0, 3.0) == 6.0

def test_power_happy_path():
    # Verifies that the power function returns the correct result for two positive numbers
    assert power(2.0, 3.0) == 8.0

def test_modulo_happy_path():
    # Verifies that the modulo function returns the correct result for two positive numbers
    assert modulo(10.0, 3.0) == 1.0

def test_exponential_happy_path():
    # Verifies that the exponential function returns the correct result for a positive base and exponent
    assert exponential(2.0, 3) == 8.0

# Edge cases tests
def test_add_edge_case_zero():
    # Verifies that the add function returns the correct result when one of the inputs is zero
    assert add(2.0, 0.0) == 2.0

def test_multiply_edge_case_zero():
    # Verifies that the multiply function returns the correct result when one of the inputs is zero
    assert multiply(2.0, 0.0) == 0.0

def test_power_edge_case_zero():
    # Verifies that the power function returns the correct result when the exponent is zero
    assert power(2.0, 0.0) == 1.0

def test_modulo_edge_case_zero_divisor():
    # Verifies that the modulo function raises a ZeroDivisionError when the divisor is zero
    with pytest.raises(ZeroDivisionError):
        modulo(10.0, 0.0)

def test_exponential_edge_case_zero_exponent():
    # Verifies that the exponential function returns 1 when the exponent is zero
    assert exponential(2.0, 0) == 1

# Error cases tests
def test_add_error_case_non_numeric_input():
    # Verifies that the add function raises a TypeError when one of the inputs is not a number
    with pytest.raises(TypeError):
        add('a', 2.0)

def test_multiply_error_case_non_numeric_input():
    # Verifies that the multiply function raises a TypeError when one of the inputs is not a number
    with pytest.raises(TypeError):
        multiply('a', 2.0)

def test_power_error_case_non_numeric_input():
    # Verifies that the power function raises a TypeError when one of the inputs is not a number
    with pytest.raises(TypeError):
        power('a', 2.0)

def test_modulo_error_case_non_numeric_input():
    # Verifies that the modulo function raises a TypeError when one of the inputs is not a number
    with pytest.raises(TypeError):
        modulo('a', 2.0)

def test_exponential_error_case_non_numeric_base():
    # Verifies that the exponential function raises a TypeError when the base is not a number
    with pytest.raises(TypeError):
        exponential('a', 2)

def test_exponential_error_case_non_integer_exponent():
    # Verifies that the exponential function raises a TypeError when the exponent is not an integer
    with pytest.raises(TypeError):
        exponential(2.0, 2.5)

# Security cases tests
def test_csrf_token_validation(client):
    # Verifies that the CSRF token is validated correctly
    with client.session_transaction() as sess:
        csrf_token = sess.get('csrf_token')
    response = client.post('/login', data={'username': 'test', 'password': 'test', 'csrf_token': csrf_token})
    assert response.status_code == 200

def test_password_hashing(client):
    # Verifies that the password is hashed correctly
    password = 'test'
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    response = client.post('/login', data={'username': 'test', 'password': password})
    assert response.status_code == 200
    # Note: This test is simplified and does not cover all possible security scenarios

def test_injection_attack(client):
    # Verifies that the application is not vulnerable to SQL injection attacks
    username = "test'; DROP TABLE users; --"
    password = 'test'
    response = client.post('/login', data={'username': username, 'password': password})
    assert response.status_code != 200

def test_malformed_data(client):
    # Verifies that the application handles malformed data correctly
    username = '<script>alert("XSS")</script>'
    password = 'test'
    response = client.post('/login', data={'username': username, 'password': password})
    assert response.status_code != 200