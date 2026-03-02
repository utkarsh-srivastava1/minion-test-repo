# tests/test_hashmap.py
import pytest
from src.hashmap import HashMap
from src.logger import Logger
import logging

# Setup and teardown
@pytest.fixture
def hashmap():
    """Create a new HashMap instance for each test"""
    return HashMap()

# Happy path
def test_get_set_key_value(hashmap):
    # Verify that setting and getting a key-value pair works as expected
    key = "test_key"
    value = "test_value"
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_get_non_existent_key(hashmap):
    # Verify that getting a non-existent key returns None
    key = "non_existent_key"
    assert hashmap.get(key) is None

# Edge cases
def test_set_empty_key(hashmap):
    # Verify that setting an empty key raises no errors
    key = ""
    value = "test_value"
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_set_none_key(hashmap):
    # Verify that setting a None key raises no errors
    key = None
    value = "test_value"
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_set_empty_value(hashmap):
    # Verify that setting an empty value raises no errors
    key = "test_key"
    value = ""
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_set_none_value(hashmap):
    # Verify that setting a None value raises no errors
    key = "test_key"
    value = None
    hashmap.set(key, value)
    assert hashmap.get(key) == value

# Error cases
def test_get_invalid_key_type(hashmap):
    # Verify that getting a key with an invalid type raises no errors
    key = 123
    assert hashmap.get(key) is None

def test_set_invalid_key_type(hashmap):
    # Verify that setting a key with an invalid type raises no errors
    key = 123
    value = "test_value"
    hashmap.set(key, value)
    assert hashmap.get(key) == value

# Security cases
def test_get_malformed_key(hashmap, caplog):
    # Verify that getting a malformed key raises no errors
    key = "\x00\x00\x00\x00"
    with caplog.at_level(logging.INFO):
        hashmap.get(key)
    assert "Getting value for key: \x00\x00\x00\x00" in caplog.text

def test_set_malformed_key(hashmap, caplog):
    # Verify that setting a malformed key raises no errors
    key = "\x00\x00\x00\x00"
    value = "test_value"
    with caplog.at_level(logging.INFO):
        hashmap.set(key, value)
    assert "Setting value for key: \x00\x00\x00\x00" in caplog.text

# Logger tests
def test_logger_info(hashmap, caplog):
    # Verify that the logger logs info messages correctly
    key = "test_key"
    with caplog.at_level(logging.INFO):
        hashmap.get(key)
    assert f"Getting value for key: {key}" in caplog.text

def test_logger_set(hashmap, caplog):
    # Verify that the logger logs set messages correctly
    key = "test_key"
    value = "test_value"
    with caplog.at_level(logging.INFO):
        hashmap.set(key, value)
    assert f"Setting value for key: {key}" in caplog.text