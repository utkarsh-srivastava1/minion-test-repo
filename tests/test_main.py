# tests/test_main.py

import pytest
from src.main import hello, add, multiply, power, modulo

def test_hello_function():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the correct result for positive numbers
    assert add(5, 7) == 12

def test_add_negative_numbers():
    # Verifies the add function returns the correct result for negative numbers
    assert add(-5, -7) == -12

def test_add_mixed_numbers():
    # Verifies the add function returns the correct result for mixed positive and negative numbers
    assert add(-5, 7) == 2

def test_add_floats():
    # Verifies the add function returns the correct result for floating point numbers
    assert add(5.5, 7.7) == 13.2

def test_add_edge_case_max_value():
    # Verifies the add function raises an OverflowError for very large numbers
    with pytest.raises(OverflowError):
        add(float('inf'), 1)

def test_add_error_case_non_numeric_input():
    # Verifies the add function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        add('a', 5)

def test_multiply_happy_path():
    # Verifies the multiply function returns the correct result for positive numbers
    assert multiply(5, 7) == 35

def test_multiply_negative_numbers():
    # Verifies the multiply function returns the correct result for negative numbers
    assert multiply(-5, -7) == 35

def test_multiply_mixed_numbers():
    # Verifies the multiply function returns the correct result for mixed positive and negative numbers
    assert multiply(-5, 7) == -35

def test_multiply_floats():
    # Verifies the multiply function returns the correct result for floating point numbers
    assert multiply(5.5, 7.7) == 42.35

def test_multiply_edge_case_max_value():
    # Verifies the multiply function raises an OverflowError for very large numbers
    with pytest.raises(OverflowError):
        multiply(float('inf'), 1)

def test_multiply_error_case_non_numeric_input():
    # Verifies the multiply function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        multiply('a', 5)

def test_power_happy_path():
    # Verifies the power function returns the correct result for positive numbers
    assert power(5, 2) == 25

def test_power_negative_numbers():
    # Verifies the power function returns the correct result for negative numbers
    assert power(-5, 2) == 25

def test_power_mixed_numbers():
    # Verifies the power function returns the correct result for mixed positive and negative numbers
    assert power(-5, 3) == -125

def test_power_floats():
    # Verifies the power function returns the correct result for floating point numbers
    assert power(5.5, 2.2) == pytest.approx(39.0625)

def test_power_edge_case_max_value():
    # Verifies the power function raises an OverflowError for very large numbers
    with pytest.raises(OverflowError):
        power(float('inf'), 1)

def test_power_error_case_non_numeric_input():
    # Verifies the power function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        power('a', 5)

def test_modulo_happy_path():
    # Verifies the modulo function returns the correct result for positive numbers
    assert modulo(17, 5) == 2

def test_modulo_negative_numbers():
    # Verifies the modulo function returns the correct result for negative numbers
    assert modulo(-17, 5) == 3

def test_modulo_mixed_numbers():
    # Verifies the modulo function returns the correct result for mixed positive and negative numbers
    assert modulo(17, -5) == 2

def test_modulo_floats():
    # Verifies the modulo function returns the correct result for floating point numbers
    assert modulo(17.7, 5.5) == pytest.approx(2.2)

def test_modulo_edge_case_division_by_zero():
    # Verifies the modulo function raises a ZeroDivisionError for division by zero
    with pytest.raises(ZeroDivisionError):
        modulo(17, 0)

def test_modulo_error_case_non_numeric_input():
    # Verifies the modulo function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        modulo('a', 5)

def test_modulo_error_case_non_numeric_divisor():
    # Verifies the modulo function raises a TypeError for non-numeric divisor
    with pytest.raises(TypeError):
        modulo(17, 'a')