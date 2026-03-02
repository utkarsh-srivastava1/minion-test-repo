# tests/test_user.py

import pytest
from src.user import User
from src.logger import Logger
import logging

# Setup and teardown
@pytest.fixture
def user():
    # Create a test user
    return User("John Doe", "john@example.com")

def test_happy_path_user_creation(user):
    # Verify that the user is created with the correct name and email
    assert user.name == "John Doe"
    assert user.email == "john@example.com"

def test_happy_path_greet(user, caplog):
    # Verify that the greet method returns the correct greeting
    # and logs an info message
    caplog.set_level(logging.INFO)
    greeting = user.greet()
    assert greeting == "Hello, John Doe"
    assert "Greeting user" in caplog.text

def test_edge_case_empty_name():
    # Verify that creating a user with an empty name raises a ValueError
    with pytest.raises(ValueError):
        User("", "john@example.com")

def test_edge_case_empty_email():
    # Verify that creating a user with an empty email raises a ValueError
    with pytest.raises(ValueError):
        User("John Doe", "")

def test_edge_case_null_name():
    # Verify that creating a user with a null name raises a TypeError
    with pytest.raises(TypeError):
        User(None, "john@example.com")

def test_edge_case_null_email():
    # Verify that creating a user with a null email raises a TypeError
    with pytest.raises(TypeError):
        User("John Doe", None)

def test_error_case_invalid_email():
    # Verify that creating a user with an invalid email raises a ValueError
    with pytest.raises(ValueError):
        User("John Doe", "invalid_email")

def test_security_case_injection_name():
    # Verify that creating a user with a malicious name does not raise an exception
    User("<script>alert('XSS')</script>", "john@example.com")

def test_security_case_injection_email():
    # Verify that creating a user with a malicious email does not raise an exception
    User("John Doe", "<script>alert('XSS')</script>")

def test_security_case_malformed_data_name():
    # Verify that creating a user with malformed name data does not raise an exception
    User(123, "john@example.com")

def test_security_case_malformed_data_email():
    # Verify that creating a user with malformed email data does not raise an exception
    User("John Doe", 123)

def test_logger_instance(user):
    # Verify that the logger instance is created correctly
    assert isinstance(user.logger, Logger)

def test_logger_name(user):
    # Verify that the logger name is set correctly
    assert user.logger.name == __name__