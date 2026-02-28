# tests/test_main.py
import pytest
from src.main import hello, add, multiply, power, modulo, exponential

def test_hello_happy_path():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the correct result for two positive numbers
    assert add(2.0, 3.0) == 5.0

def test_add_negative_numbers():
    # Verifies the add function returns the correct result for two negative numbers
    assert add(-2.0, -3.0) == -5.0

def test_add_mixed_numbers():
    # Verifies the add function returns the correct result for a positive and a negative number
    assert add(2.0, -3.0) == -1.0

def test_add_edge_case_zero():
    # Verifies the add function returns the correct result when one of the inputs is zero
    assert add(2.0, 0.0) == 2.0

def test_add_error_case_non_numeric_input():
    # Verifies the add function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        add('a', 2.0)

def test_add_error_case_overflow():
    # Verifies the add function raises an OverflowError when the result is too large
    with pytest.raises(OverflowError):
        add(float('inf'), 2.0)

def test_multiply_happy_path():
    # Verifies the multiply function returns the correct result for two positive numbers
    assert multiply(2.0, 3.0) == 6.0

def test_multiply_negative_numbers():
    # Verifies the multiply function returns the correct result for two negative numbers
    assert multiply(-2.0, -3.0) == 6.0

def test_multiply_mixed_numbers():
    # Verifies the multiply function returns the correct result for a positive and a negative number
    assert multiply(2.0, -3.0) == -6.0

def test_multiply_edge_case_zero():
    # Verifies the multiply function returns the correct result when one of the inputs is zero
    assert multiply(2.0, 0.0) == 0.0

def test_multiply_error_case_non_numeric_input():
    # Verifies the multiply function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        multiply('a', 2.0)

def test_multiply_error_case_overflow():
    # Verifies the multiply function raises an OverflowError when the result is too large
    with pytest.raises(OverflowError):
        multiply(float('inf'), 2.0)

def test_power_happy_path():
    # Verifies the power function returns the correct result for a positive base and exponent
    assert power(2.0, 3.0) == 8.0

def test_power_negative_base():
    # Verifies the power function returns the correct result for a negative base and exponent
    assert power(-2.0, 3.0) == -8.0

def test_power_negative_exponent():
    # Verifies the power function returns the correct result for a positive base and negative exponent
    assert power(2.0, -3.0) == 0.125

def test_power_edge_case_zero():
    # Verifies the power function returns the correct result when the base is zero and the exponent is positive
    assert power(0.0, 2.0) == 0.0

def test_power_error_case_non_numeric_input():
    # Verifies the power function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        power('a', 2.0)

def test_power_error_case_overflow():
    # Verifies the power function raises an OverflowError when the result is too large
    with pytest.raises(OverflowError):
        power(float('inf'), 2.0)

def test_modulo_happy_path():
    # Verifies the modulo function returns the correct result for two positive numbers
    assert modulo(10.0, 3.0) == 1.0

def test_modulo_negative_numbers():
    # Verifies the modulo function returns the correct result for two negative numbers
    assert modulo(-10.0, -3.0) == -1.0

def test_modulo_mixed_numbers():
    # Verifies the modulo function returns the correct result for a positive and a negative number
    assert modulo(10.0, -3.0) == 1.0

def test_modulo_edge_case_zero():
    # Verifies the modulo function raises a ZeroDivisionError when the divisor is zero
    with pytest.raises(ZeroDivisionError):
        modulo(10.0, 0.0)

def test_modulo_error_case_non_numeric_input():
    # Verifies the modulo function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        modulo('a', 2.0)

def test_exponential_happy_path():
    # Verifies the exponential function returns the correct result for a positive base and exponent
    assert exponential(2.0, 3) == 8.0

def test_exponential_negative_base():
    # Verifies the exponential function returns the correct result for a negative base and exponent
    assert exponential(-2.0, 3) == -8.0

def test_exponential_negative_exponent():
    # Verifies the exponential function returns the correct result for a positive base and negative exponent
    assert exponential(2.0, -3) == 0.125

def test_exponential_edge_case_zero():
    # Verifies the exponential function returns the correct result when the base is zero and the exponent is positive
    assert exponential(0.0, 2) == 0.0

def test_exponential_error_case_non_numeric_input():
    # Verifies the exponential function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        exponential('a', 2)

def test_exponential_error_case_non_integer_exponent():
    # Verifies the exponential function raises a TypeError when the exponent is not an integer
    with pytest.raises(TypeError):
        exponential(2.0, 2.5)