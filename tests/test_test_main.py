# tests/test_main.py

import pytest
from src.main import hello, add, multiply, power, modulo


def test_hello_function_returns_hello_world():
    # Verifies the hello function returns the expected string
    assert hello() == 'Hello World'


def test_add_function_happy_path():
    # Verifies the add function works with normal inputs
    assert add(1, 2) == 3
    assert add(1.5, 2.5) == 4


def test_add_function_edge_cases():
    # Verifies the add function handles edge cases
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_add_function_error_cases():
    # Verifies the add function raises errors with invalid inputs
    with pytest.raises(TypeError):
        add('a', 2)
    with pytest.raises(TypeError):
        add(1, 'b')
    with pytest.raises(OverflowError):
        add(float('inf'), 1)


def test_multiply_function_happy_path():
    # Verifies the multiply function works with normal inputs
    assert multiply(1, 2) == 2
    assert multiply(1.5, 2.5) == 3.75


def test_multiply_function_edge_cases():
    # Verifies the multiply function handles edge cases
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1


def test_multiply_function_error_cases():
    # Verifies the multiply function raises errors with invalid inputs
    with pytest.raises(TypeError):
        multiply('a', 2)
    with pytest.raises(TypeError):
        multiply(1, 'b')
    with pytest.raises(OverflowError):
        multiply(float('inf'), 1)


def test_power_function_happy_path():
    # Verifies the power function works with normal inputs
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(2, -1) == 0.5


def test_power_function_edge_cases():
    # Verifies the power function handles edge cases
    assert power(0, 0) == 1  # By convention, 0^0 = 1
    assert power(1, 1) == 1
    assert power(-1, 1) == -1


def test_power_function_error_cases():
    # Verifies the power function raises errors with invalid inputs
    with pytest.raises(TypeError):
        power('a', 2)
    with pytest.raises(TypeError):
        power(1, 'b')
    with pytest.raises(OverflowError):
        power(float('inf'), 1)


def test_power_function_negative_exponent():
    # Verifies the power function handles negative exponents
    assert power(2, -1) == 0.5
    assert power(2, -2) == 0.25


def test_power_function_non_integer_exponent():
    # Verifies the power function handles non-integer exponents
    assert power(2, 0.5) == 2 ** 0.5
    assert power(2, 1.5) == 2 ** 1.5


def test_power_function_zero_base():
    # Verifies the power function handles zero base
    assert power(0, 1) == 0
    assert power(0, -1) == float('inf')


def test_power_function_negative_base():
    # Verifies the power function handles negative base
    assert power(-2, 1) == -2
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8


def test_power_function_non_numeric_inputs():
    # Verifies the power function raises errors with non-numeric inputs
    with pytest.raises(TypeError):
        power('a', 2)
    with pytest.raises(TypeError):
        power(1, 'b')
    with pytest.raises(TypeError):
        power(None, 2)
    with pytest.raises(TypeError):
        power(1, None)


def test_modulo_function_happy_path():
    # Verifies the modulo function works with normal inputs
    assert modulo(10, 3) == 1
    assert modulo(10, 5) == 0


def test_modulo_function_edge_cases():
    # Verifies the modulo function handles edge cases
    assert modulo(0, 1) == 0
    assert modulo(1, 1) == 0


def test_modulo_function_error_cases():
    # Verifies the modulo function raises errors with invalid inputs
    with pytest.raises(TypeError):
        modulo('a', 2)
    with pytest.raises(TypeError):
        modulo(1, 'b')
    with pytest.raises(ZeroDivisionError):
        modulo(1, 0)


def test_modulo_function_division_by_zero():
    # Verifies the modulo function raises ZeroDivisionError when dividing by zero
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)


def test_modulo_function_non_numeric_inputs():
    # Verifies the modulo function raises TypeError with non-numeric inputs
    with pytest.raises(TypeError):
        modulo('a', 2)
    with pytest.raises(TypeError):
        modulo(1, 'b')
    with pytest.raises(TypeError):
        modulo(None, 2)
    with pytest.raises(TypeError):
        modulo(1, None)


def test_modulo_function_negative_inputs():
    # Verifies the modulo function handles negative inputs
    assert modulo(-10, 3) == 2
    assert modulo(10, -3) == 1


def test_modulo_function_float_inputs():
    # Verifies the modulo function handles float inputs
    assert modulo(10.5, 3) == 1.5
    assert modulo(10, 3.5) == 3.0


def test_modulo_function_large_inputs():
    # Verifies the modulo function handles large inputs
    assert modulo(1000000, 3) == 1
    assert modulo(1000000, 1000000) == 0