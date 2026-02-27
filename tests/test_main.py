# tests/test_main.py

import pytest
from src.main import hello, add, multiply, power, factorial

def test_hello_happy_path():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the expected result for two positive numbers
    assert add(2, 3) == 5

def test_add_negative_numbers():
    # Verifies the add function returns the expected result for two negative numbers
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    # Verifies the add function returns the expected result for a positive and a negative number
    assert add(2, -3) == -1

def test_add_floats():
    # Verifies the add function returns the expected result for two float numbers
    assert add(2.5, 3.7) == 6.2

def test_add_edge_case_zero():
    # Verifies the add function returns the expected result for adding zero
    assert add(2, 0) == 2

def test_add_error_case_non_numeric_input():
    # Verifies the add function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        add('a', 3)

def test_multiply_happy_path():
    # Verifies the multiply function returns the expected result for two positive numbers
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    # Verifies the multiply function returns the expected result for two negative numbers
    assert multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    # Verifies the multiply function returns the expected result for a positive and a negative number
    assert multiply(2, -3) == -6

def test_multiply_floats():
    # Verifies the multiply function returns the expected result for two float numbers
    assert multiply(2.5, 3.7) == 9.25

def test_multiply_edge_case_zero():
    # Verifies the multiply function returns the expected result for multiplying by zero
    assert multiply(2, 0) == 0

def test_multiply_error_case_non_numeric_input():
    # Verifies the multiply function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        multiply('a', 3)

def test_power_happy_path():
    # Verifies the power function returns the expected result for two positive numbers
    assert power(2, 3) == 8

def test_power_negative_numbers():
    # Verifies the power function returns the expected result for a negative base and a positive exponent
    assert power(-2, 3) == -8

def test_power_mixed_numbers():
    # Verifies the power function returns the expected result for a positive base and a negative exponent
    assert power(2, -3) == 1/8

def test_power_floats():
    # Verifies the power function returns the expected result for two float numbers
    assert power(2.5, 3.7) == pytest.approx(2.5 ** 3.7)

def test_power_edge_case_zero():
    # Verifies the power function returns the expected result for a zero base and a positive exponent
    assert power(0, 3) == 0

def test_power_error_case_non_numeric_input():
    # Verifies the power function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        power('a', 3)

def test_factorial_happy_path():
    # Verifies the factorial function returns the expected result for a positive integer
    assert factorial(5) == 120

def test_factorial_edge_case_zero():
    # Verifies the factorial function returns the expected result for zero
    assert factorial(0) == 1

def test_factorial_edge_case_one():
    # Verifies the factorial function returns the expected result for one
    assert factorial(1) == 1

def test_factorial_error_case_negative_input():
    # Verifies the factorial function raises a ValueError for a negative input
    with pytest.raises(ValueError):
        factorial(-3)

def test_factorial_error_case_non_integer_input():
    # Verifies the factorial function raises a TypeError for a non-integer input
    with pytest.raises(TypeError):
        factorial(3.7)

def test_factorial_error_case_non_numeric_input():
    # Verifies the factorial function raises a TypeError for a non-numeric input
    with pytest.raises(TypeError):
        factorial('a')