# tests/test_main.py
import pytest
from src.main import hello, add, multiply

# Happy path tests
def test_hello_function_returns_hello_world():
    # Verifies the hello function returns 'Hello World'
    assert hello() == 'Hello World'

def test_add_function_returns_sum_of_two_numbers():
    # Verifies the add function returns the sum of two numbers
    assert add(2, 3) == 5

def test_multiply_function_returns_product_of_two_numbers():
    # Verifies the multiply function returns the product of two numbers
    assert multiply(2, 3) == 6

# Edge cases tests
def test_add_function_with_zero():
    # Verifies the add function handles zero correctly
    assert add(0, 0) == 0

def test_multiply_function_with_zero():
    # Verifies the multiply function handles zero correctly
    assert multiply(0, 10) == 0

def test_add_function_with_negative_numbers():
    # Verifies the add function handles negative numbers correctly
    assert add(-2, -3) == -5

def test_multiply_function_with_negative_numbers():
    # Verifies the multiply function handles negative numbers correctly
    assert multiply(-2, -3) == 6

def test_add_function_with_floats():
    # Verifies the add function handles floats correctly
    assert add(2.5, 3.7) == 6.2

def test_multiply_function_with_floats():
    # Verifies the multiply function handles floats correctly
    assert multiply(2.5, 3.7) == 9.25

# Error cases tests
def test_add_function_with_non_numeric_input():
    # Verifies the add function raises a TypeError with non-numeric input
    with pytest.raises(TypeError):
        add('a', 2)

def test_multiply_function_with_non_numeric_input():
    # Verifies the multiply function raises a TypeError with non-numeric input
    with pytest.raises(TypeError):
        multiply('a', 2)

def test_add_function_with_none_input():
    # Verifies the add function raises a TypeError with None input
    with pytest.raises(TypeError):
        add(None, 2)

def test_multiply_function_with_none_input():
    # Verifies the multiply function raises a TypeError with None input
    with pytest.raises(TypeError):
        multiply(None, 2)

# Security cases tests
def test_add_function_with_malformed_input():
    # Verifies the add function raises a TypeError with malformed input
    with pytest.raises(TypeError):
        add([1, 2], 3)

def test_multiply_function_with_malformed_input():
    # Verifies the multiply function raises a TypeError with malformed input
    with pytest.raises(TypeError):
        multiply([1, 2], 3)

# Setup/Teardown tests
@pytest.fixture
def setup_add_function():
    # Setup for add function tests
    yield
    # Teardown for add function tests

def test_add_function_with_setup_teardown(setup_add_function):
    # Verifies the add function works correctly with setup and teardown
    assert add(2, 3) == 5

# Isolation tests
def test_add_function_isolation():
    # Verifies the add function does not affect other functions
    assert add(2, 3) == 5
    assert hello() == 'Hello World'

def test_multiply_function_isolation():
    # Verifies the multiply function does not affect other functions
    assert multiply(2, 3) == 6
    assert hello() == 'Hello World'