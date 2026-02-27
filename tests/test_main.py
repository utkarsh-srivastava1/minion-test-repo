# tests/test_main.py

import pytest
from src.main import hello, add, multiply, power, modulo, exponential

def test_hello_happy_path():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the expected result for positive numbers
    assert add(2, 3) == 5

def test_add_negative_numbers():
    # Verifies the add function returns the expected result for negative numbers
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    # Verifies the add function returns the expected result for mixed numbers
    assert add(-2, 3) == 1

def test_add_edge_case_zero():
    # Verifies the add function returns the expected result for zero
    assert add(0, 0) == 0

def test_add_error_case_non_numeric_input():
    # Verifies the add function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        add('a', 2)

def test_multiply_happy_path():
    # Verifies the multiply function returns the expected result for positive numbers
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    # Verifies the multiply function returns the expected result for negative numbers
    assert multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    # Verifies the multiply function returns the expected result for mixed numbers
    assert multiply(-2, 3) == -6

def test_multiply_edge_case_zero():
    # Verifies the multiply function returns the expected result for zero
    assert multiply(0, 0) == 0

def test_multiply_error_case_non_numeric_input():
    # Verifies the multiply function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        multiply('a', 2)

def test_power_happy_path():
    # Verifies the power function returns the expected result for positive numbers
    assert power(2, 3) == 8

def test_power_negative_numbers():
    # Verifies the power function returns the expected result for negative numbers
    assert power(-2, 3) == -8

def test_power_mixed_numbers():
    # Verifies the power function returns the expected result for mixed numbers
    assert power(-2, 2) == 4

def test_power_edge_case_zero():
    # Verifies the power function returns the expected result for zero
    assert power(0, 0) == 1

def test_power_error_case_non_numeric_input():
    # Verifies the power function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        power('a', 2)

def test_modulo_happy_path():
    # Verifies the modulo function returns the expected result for positive numbers
    assert modulo(10, 3) == 1

def test_modulo_negative_numbers():
    # Verifies the modulo function returns the expected result for negative numbers
    assert modulo(-10, 3) == 2

def test_modulo_mixed_numbers():
    # Verifies the modulo function returns the expected result for mixed numbers
    assert modulo(-10, -3) == -1

def test_modulo_edge_case_zero():
    # Verifies the modulo function raises a ZeroDivisionError for zero divisor
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)

def test_modulo_error_case_non_numeric_input():
    # Verifies the modulo function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        modulo('a', 2)

def test_exponential_happy_path():
    # Verifies the exponential function returns the expected result for positive numbers
    assert exponential(2, 3) == 8

def test_exponential_negative_numbers():
    # Verifies the exponential function returns the expected result for negative numbers
    assert exponential(-2, 3) == -8

def test_exponential_mixed_numbers():
    # Verifies the exponential function returns the expected result for mixed numbers
    assert exponential(-2, 2) == 4

def test_exponential_edge_case_zero():
    # Verifies the exponential function returns the expected result for zero
    assert exponential(0, 0) == 1

def test_exponential_error_case_non_numeric_input():
    # Verifies the exponential function raises a TypeError for non-numeric input
    with pytest.raises(TypeError):
        exponential('a', 2)

def test_exponential_error_case_non_integer_exponent():
    # Verifies the exponential function raises a TypeError for non-integer exponent
    with pytest.raises(TypeError):
        exponential(2, 2.5)

def test_exponential_large_input():
    # Verifies the exponential function returns the expected result for large input
    assert exponential(2, 10) == 1024

def test_exponential_negative_exponent():
    # Verifies the exponential function returns the expected result for negative exponent
    assert exponential(2, -3) == 0.125