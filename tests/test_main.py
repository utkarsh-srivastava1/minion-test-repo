# tests/test_main.py
import pytest
from src.main import hello, add, multiply, power, modulo, exponential, square_root

def test_hello_happy_path():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path():
    # Verifies the add function returns the correct result for two positive numbers
    assert add(2.0, 3.0) == 5.0

def test_add_edge_case_zero():
    # Verifies the add function returns the correct result when one of the inputs is zero
    assert add(2.0, 0.0) == 2.0

def test_add_edge_case_negative():
    # Verifies the add function returns the correct result for two negative numbers
    assert add(-2.0, -3.0) == -5.0

def test_add_error_case_non_numeric_input():
    # Verifies the add function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        add('a', 2.0)

def test_multiply_happy_path():
    # Verifies the multiply function returns the correct result for two positive numbers
    assert multiply(2.0, 3.0) == 6.0

def test_multiply_edge_case_zero():
    # Verifies the multiply function returns the correct result when one of the inputs is zero
    assert multiply(2.0, 0.0) == 0.0

def test_multiply_edge_case_negative():
    # Verifies the multiply function returns the correct result for two negative numbers
    assert multiply(-2.0, -3.0) == 6.0

def test_multiply_error_case_non_numeric_input():
    # Verifies the multiply function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        multiply('a', 2.0)

def test_power_happy_path():
    # Verifies the power function returns the correct result for two positive numbers
    assert power(2.0, 3.0) == 8.0

def test_power_edge_case_zero_exponent():
    # Verifies the power function returns the correct result when the exponent is zero
    assert power(2.0, 0.0) == 1.0

def test_power_edge_case_negative_exponent():
    # Verifies the power function returns the correct result for a negative exponent
    assert power(2.0, -3.0) == 0.125

def test_power_error_case_non_numeric_input():
    # Verifies the power function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        power('a', 2.0)

def test_modulo_happy_path():
    # Verifies the modulo function returns the correct result for two positive numbers
    assert modulo(10.0, 3.0) == 1.0

def test_modulo_edge_case_zero_divisor():
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

def test_exponential_edge_case_zero_exponent():
    # Verifies the exponential function returns the correct result when the exponent is zero
    assert exponential(2.0, 0) == 1.0

def test_exponential_edge_case_negative_exponent():
    # Verifies the exponential function returns the correct result for a negative exponent
    assert exponential(2.0, -3) == 0.125

def test_exponential_error_case_non_numeric_base():
    # Verifies the exponential function raises a TypeError when a non-numeric base is provided
    with pytest.raises(TypeError):
        exponential('a', 2)

def test_exponential_error_case_non_integer_exponent():
    # Verifies the exponential function raises a TypeError when a non-integer exponent is provided
    with pytest.raises(TypeError):
        exponential(2.0, 2.5)

def test_square_root_happy_path():
    # Verifies the square_root function returns the correct result for a positive number
    assert square_root(4.0) == 2.0

def test_square_root_edge_case_zero():
    # Verifies the square_root function returns the correct result when the input is zero
    assert square_root(0.0) == 0.0

def test_square_root_error_case_negative_input():
    # Verifies the square_root function raises a ValueError when a negative input is provided
    with pytest.raises(ValueError):
        square_root(-4.0)

def test_square_root_error_case_non_numeric_input():
    # Verifies the square_root function raises a TypeError when a non-numeric input is provided
    with pytest.raises(TypeError):
        square_root('a')