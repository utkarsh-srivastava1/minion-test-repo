# tests/test_main.py
import pytest
from src.main import hello, add, subtract

# Happy path tests
def test_hello_function_returns_hello_world():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_function_returns_sum_of_two_numbers():
    # Verifies the add function returns the sum of two numbers
    assert add(5, 3) == 8

def test_subtract_function_returns_difference_of_two_numbers():
    # Verifies the subtract function returns the difference of two numbers
    assert subtract(10, 4) == 6

# Edge cases tests
def test_add_function_with_zero():
    # Verifies the add function handles zero correctly
    assert add(0, 0) == 0

def test_subtract_function_with_zero():
    # Verifies the subtract function handles zero correctly
    assert subtract(0, 0) == 0

def test_add_function_with_negative_numbers():
    # Verifies the add function handles negative numbers correctly
    assert add(-5, -3) == -8

def test_subtract_function_with_negative_numbers():
    # Verifies the subtract function handles negative numbers correctly
    assert subtract(-10, -4) == -6

def test_add_function_with_floats():
    # Verifies the add function handles floats correctly
    assert add(5.5, 3.3) == 8.8

def test_subtract_function_with_floats():
    # Verifies the subtract function handles floats correctly
    assert subtract(10.5, 4.3) == 6.2

# Error cases tests
def test_add_function_with_non_numeric_inputs():
    # Verifies the add function raises an error with non-numeric inputs
    with pytest.raises(TypeError):
        add('a', 3)

def test_subtract_function_with_non_numeric_inputs():
    # Verifies the subtract function raises an error with non-numeric inputs
    with pytest.raises(TypeError):
        subtract('a', 3)

def test_add_function_with_none_inputs():
    # Verifies the add function raises an error with None inputs
    with pytest.raises(TypeError):
        add(None, 3)

def test_subtract_function_with_none_inputs():
    # Verifies the subtract function raises an error with None inputs
    with pytest.raises(TypeError):
        subtract(None, 3)

# Security cases tests
def test_add_function_with_malformed_data():
    # Verifies the add function raises an error with malformed data
    with pytest.raises(TypeError):
        add([1, 2], 3)

def test_subtract_function_with_malformed_data():
    # Verifies the subtract function raises an error with malformed data
    with pytest.raises(TypeError):
        subtract([1, 2], 3)

# Setup and teardown
@pytest.fixture
def setup_and_teardown():
    # Setup code
    print("Setup")
    yield
    # Teardown code
    print("Teardown")

def test_hello_function_with_setup_and_teardown(setup_and_teardown):
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'