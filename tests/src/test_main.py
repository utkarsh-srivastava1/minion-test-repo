# tests/test_main.py

import pytest
from src.main import hello, add, divide

def test_hello_happy_path():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the correct sum
    assert add(2, 3) == 5

def test_divide_happy_path():
    # Verifies the divide function returns the correct quotient
    assert divide(10, 2) == 5

def test_add_edge_case_empty_inputs():
    # Verifies the add function handles empty inputs correctly
    with pytest.raises(TypeError):
        add()

def test_add_edge_case_null_inputs():
    # Verifies the add function handles null inputs correctly
    with pytest.raises(TypeError):
        add(None, 2)

def test_divide_edge_case_null_inputs():
    # Verifies the divide function handles null inputs correctly
    with pytest.raises(TypeError):
        divide(None, 2)

def test_divide_edge_case_empty_inputs():
    # Verifies the divide function handles empty inputs correctly
    with pytest.raises(TypeError):
        divide()

def test_divide_edge_case_non_numeric_inputs():
    # Verifies the divide function handles non-numeric inputs correctly
    with pytest.raises(TypeError):
        divide('a', 2)

def test_divide_error_case_division_by_zero():
    # Verifies the divide function raises a ZeroDivisionError when dividing by zero
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_error_case_invalid_input_type():
    # Verifies the divide function raises a TypeError when input type is invalid
    with pytest.raises(TypeError):
        divide('a', 'b')

def test_add_error_case_invalid_input_type():
    # Verifies the add function raises a TypeError when input type is invalid
    with pytest.raises(TypeError):
        add('a', 'b')

def test_hello_security_case_injection():
    # Verifies the hello function does not allow injection attacks
    assert hello() == 'Hello World'

def test_add_security_case_injection():
    # Verifies the add function does not allow injection attacks
    assert add(2, 3) == 5

def test_divide_security_case_injection():
    # Verifies the divide function does not allow injection attacks
    assert divide(10, 2) == 5

def test_add_security_case_malformed_data():
    # Verifies the add function handles malformed data correctly
    with pytest.raises(TypeError):
        add([1, 2], 3)

def test_divide_security_case_malformed_data():
    # Verifies the divide function handles malformed data correctly
    with pytest.raises(TypeError):
        divide([1, 2], 3)