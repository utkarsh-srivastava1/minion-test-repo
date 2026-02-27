# tests/test_main.py

import pytest
from src.main import hello, add, multiply, power, modulo, sum_of_natural_numbers

def test_hello_happy_path():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the correct result for two positive numbers
    assert add(2, 3) == 5

def test_add_negative_numbers():
    # Verifies the add function returns the correct result for two negative numbers
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    # Verifies the add function returns the correct result for a positive and a negative number
    assert add(2, -3) == -1

def test_add_edge_case_zero():
    # Verifies the add function returns the correct result when one of the inputs is zero
    assert add(2, 0) == 2

def test_add_error_case_non_numeric_input():
    # Verifies the add function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        add('a', 2)

def test_multiply_happy_path():
    # Verifies the multiply function returns the correct result for two positive numbers
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    # Verifies the multiply function returns the correct result for two negative numbers
    assert multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    # Verifies the multiply function returns the correct result for a positive and a negative number
    assert multiply(2, -3) == -6

def test_multiply_edge_case_zero():
    # Verifies the multiply function returns the correct result when one of the inputs is zero
    assert multiply(2, 0) == 0

def test_multiply_error_case_non_numeric_input():
    # Verifies the multiply function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        multiply('a', 2)

def test_power_happy_path():
    # Verifies the power function returns the correct result for two positive numbers
    assert power(2, 3) == 8

def test_power_negative_numbers():
    # Verifies the power function returns the correct result for a negative base and a positive exponent
    assert power(-2, 3) == -8

def test_power_mixed_numbers():
    # Verifies the power function returns the correct result for a positive base and a negative exponent
    assert power(2, -3) == 1/8

def test_power_edge_case_zero():
    # Verifies the power function returns the correct result when the base is zero and the exponent is positive
    assert power(0, 2) == 0

def test_power_error_case_non_numeric_input():
    # Verifies the power function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        power('a', 2)

def test_modulo_happy_path():
    # Verifies the modulo function returns the correct result for two positive numbers
    assert modulo(10, 3) == 1

def test_modulo_negative_numbers():
    # Verifies the modulo function returns the correct result for a negative dividend and a positive divisor
    assert modulo(-10, 3) == 2

def test_modulo_mixed_numbers():
    # Verifies the modulo function returns the correct result for a positive dividend and a negative divisor
    assert modulo(10, -3) == 1

def test_modulo_edge_case_zero():
    # Verifies the modulo function raises a ZeroDivisionError when the divisor is zero
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)

def test_modulo_error_case_non_numeric_input():
    # Verifies the modulo function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        modulo('a', 2)

def test_sum_of_natural_numbers_happy_path():
    # Verifies the sum_of_natural_numbers function returns the correct result for a positive integer
    assert sum_of_natural_numbers(5) == 15

def test_sum_of_natural_numbers_edge_case_one():
    # Verifies the sum_of_natural_numbers function returns the correct result for the input 1
    assert sum_of_natural_numbers(1) == 1

def test_sum_of_natural_numbers_error_case_non_integer_input():
    # Verifies the sum_of_natural_numbers function raises a TypeError when a non-integer input is provided
    with pytest.raises(TypeError):
        sum_of_natural_numbers(2.5)

def test_sum_of_natural_numbers_error_case_negative_input():
    # Verifies the sum_of_natural_numbers function raises a ValueError when a negative input is provided
    with pytest.raises(ValueError):
        sum_of_natural_numbers(-1)

def test_sum_of_natural_numbers_error_case_zero():
    # Verifies the sum_of_natural_numbers function raises a ValueError when the input is zero
    with pytest.raises(ValueError):
        sum_of_natural_numbers(0)