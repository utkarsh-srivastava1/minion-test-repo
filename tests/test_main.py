# tests/test_main.py

import pytest
from src.main import hello, add, multiply

def test_hello_happy_path():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the correct result for two positive numbers
    assert add(2.0, 3.0) == 5.0

def test_add_happy_path_negative_numbers():
    # Verifies the add function returns the correct result for two negative numbers
    assert add(-2.0, -3.0) == -5.0

def test_add_happy_path_mixed_numbers():
    # Verifies the add function returns the correct result for a positive and a negative number
    assert add(2.0, -3.0) == -1.0

def test_multiply_happy_path():
    # Verifies the multiply function returns the correct result for two positive numbers
    assert multiply(2.0, 3.0) == 6.0

def test_multiply_happy_path_negative_numbers():
    # Verifies the multiply function returns the correct result for two negative numbers
    assert multiply(-2.0, -3.0) == 6.0

def test_multiply_happy_path_mixed_numbers():
    # Verifies the multiply function returns the correct result for a positive and a negative number
    assert multiply(2.0, -3.0) == -6.0

def test_add_edge_case_zero():
    # Verifies the add function returns the correct result when one of the inputs is zero
    assert add(0.0, 3.0) == 3.0

def test_multiply_edge_case_zero():
    # Verifies the multiply function returns the correct result when one of the inputs is zero
    assert multiply(0.0, 3.0) == 0.0

def test_add_edge_case_large_numbers():
    # Verifies the add function raises an OverflowError when the result is too large
    with pytest.raises(OverflowError):
        add(1e308, 1e308)

def test_multiply_edge_case_large_numbers():
    # Verifies the multiply function raises an OverflowError when the result is too large
    with pytest.raises(OverflowError):
        multiply(1e308, 1e308)

def test_add_error_case_non_numeric_input():
    # Verifies the add function raises a TypeError when one of the inputs is not a number
    with pytest.raises(TypeError):
        add('a', 3.0)

def test_multiply_error_case_non_numeric_input():
    # Verifies the multiply function raises a TypeError when one of the inputs is not a number
    with pytest.raises(TypeError):
        multiply('a', 3.0)

def test_add_error_case_none_input():
    # Verifies the add function raises a TypeError when one of the inputs is None
    with pytest.raises(TypeError):
        add(None, 3.0)

def test_multiply_error_case_none_input():
    # Verifies the multiply function raises a TypeError when one of the inputs is None
    with pytest.raises(TypeError):
        multiply(None, 3.0)

def test_add_security_case_injection():
    # Verifies the add function does not allow code injection
    with pytest.raises(TypeError):
        add('__import__("os").system("ls")', 3.0)

def test_multiply_security_case_injection():
    # Verifies the multiply function does not allow code injection
    with pytest.raises(TypeError):
        multiply('__import__("os").system("ls")', 3.0)