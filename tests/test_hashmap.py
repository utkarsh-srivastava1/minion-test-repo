# tests/test_hashmap.py

import pytest
from src.hashmap import HashMap

@pytest.fixture
def hashmap():
    """Setup a new HashMap instance for each test"""
    return HashMap()

def test_hashmap_get_set_happy_path(hashmap):
    # Verify get and set methods work as expected
    key = "test_key"
    value = "test_value"
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_hashmap_get_empty_key(hashmap):
    # Verify get method returns None for an empty key
    assert hashmap.get("") is None

def test_hashmap_get_none_key(hashmap):
    # Verify get method returns None for a None key
    assert hashmap.get(None) is None

def test_hashmap_set_empty_key(hashmap):
    # Verify set method works with an empty key
    key = ""
    value = "test_value"
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_hashmap_set_none_key(hashmap):
    # Verify set method works with a None key
    key = None
    value = "test_value"
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_hashmap_set_empty_value(hashmap):
    # Verify set method works with an empty value
    key = "test_key"
    value = ""
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_hashmap_set_none_value(hashmap):
    # Verify set method works with a None value
    key = "test_key"
    value = None
    hashmap.set(key, value)
    assert hashmap.get(key) == value

def test_hashmap_get_multiple_keys(hashmap):
    # Verify get method works with multiple keys
    key1 = "test_key1"
    value1 = "test_value1"
    key2 = "test_key2"
    value2 = "test_value2"
    hashmap.set(key1, value1)
    hashmap.set(key2, value2)
    assert hashmap.get(key1) == value1
    assert hashmap.get(key2) == value2

def test_hashmap_set_multiple_keys(hashmap):
    # Verify set method works with multiple keys
    key1 = "test_key1"
    value1 = "test_value1"
    key2 = "test_key2"
    value2 = "test_value2"
    hashmap.set(key1, value1)
    hashmap.set(key2, value2)
    assert hashmap.get(key1) == value1
    assert hashmap.get(key2) == value2

def test_hashmap_get_non_existent_key(hashmap):
    # Verify get method returns None for a non-existent key
    key = "non_existent_key"
    assert hashmap.get(key) is None

def test_hashmap_set_update_value(hashmap):
    # Verify set method updates the value for an existing key
    key = "test_key"
    value1 = "test_value1"
    value2 = "test_value2"
    hashmap.set(key, value1)
    hashmap.set(key, value2)
    assert hashmap.get(key) == value2

def test_hashmap_error_case_invalid_key_type(hashmap):
    # Verify set method raises a TypeError for an invalid key type
    key = 123
    value = "test_value"
    with pytest.raises(TypeError):
        hashmap.set(key, value)

def test_hashmap_error_case_invalid_value_type(hashmap):
    # Verify set method raises a TypeError for an invalid value type
    key = "test_key"
    value = 123
    with pytest.raises(TypeError):
        hashmap.set(key, value)

def test_hashmap_security_case_injection_attack(hashmap):
    # Verify set method is not vulnerable to injection attacks
    key = "__import__('os').system('ls')"
    value = "test_value"
    with pytest.raises(TypeError):
        hashmap.set(key, value)

def test_hashmap_security_case_malformed_data(hashmap):
    # Verify set method is not vulnerable to malformed data
    key = "test_key"
    value = b"malformed_data"
    with pytest.raises(TypeError):
        hashmap.set(key, value)