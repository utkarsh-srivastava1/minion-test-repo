# tests/test_main.py
import pytest
from src.main import hello, add, multiply, power, modulo, exponential
from src.logger import Logger
import logging
import io
import sys

# Setup/Teardown
@pytest.fixture
def logger():
    logger = Logger(__name__)
    yield logger

# Happy Path
def test_hello_happy_path():
    # Verifies that the hello function returns the expected string
    assert hello() == 'Hello World'

def test_add_happy_path(logger):
    # Verifies that the add function returns the correct result for two numbers
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = add(2, 3)
    assert result == 5
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_multiply_happy_path(logger):
    # Verifies that the multiply function returns the correct result for two numbers
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = multiply(2, 3)
    assert result == 6
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_power_happy_path(logger):
    # Verifies that the power function returns the correct result for two numbers
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = power(2, 3)
    assert result == 8
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_modulo_happy_path(logger):
    # Verifies that the modulo function returns the correct result for two numbers
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = modulo(10, 3)
    assert result == 1
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_exponential_happy_path(logger):
    # Verifies that the exponential function returns the correct result for a number and an exponent
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = exponential(2, 3)
    assert result == 8
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

# Edge Cases
def test_add_edge_case_zero(logger):
    # Verifies that the add function returns the correct result for zero
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = add(0, 0)
    assert result == 0
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_multiply_edge_case_zero(logger):
    # Verifies that the multiply function returns the correct result for zero
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = multiply(0, 3)
    assert result == 0
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_power_edge_case_zero(logger):
    # Verifies that the power function returns the correct result for zero
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = power(2, 0)
    assert result == 1
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_modulo_edge_case_zero_divisor(logger):
    # Verifies that the modulo function raises a ZeroDivisionError for a zero divisor
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_exponential_edge_case_zero_exponent(logger):
    # Verifies that the exponential function returns the correct result for a zero exponent
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    result = exponential(2, 0)
    assert result == 1
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

# Error Cases
def test_add_error_case_non_numeric_input(logger):
    # Verifies that the add function raises a TypeError for non-numeric input
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        add('a', 3)
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_multiply_error_case_non_numeric_input(logger):
    # Verifies that the multiply function raises a TypeError for non-numeric input
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        multiply('a', 3)
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_power_error_case_non_numeric_input(logger):
    # Verifies that the power function raises a TypeError for non-numeric input
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        power('a', 3)
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_modulo_error_case_non_numeric_input(logger):
    # Verifies that the modulo function raises a TypeError for non-numeric input
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        modulo('a', 3)
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_exponential_error_case_non_numeric_input(logger):
    # Verifies that the exponential function raises a TypeError for non-numeric input
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        exponential('a', 3)
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

# Security Cases
def test_add_security_case_injection(logger):
    # Verifies that the add function does not allow injection attacks
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        add(2, '3 + 1')
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_multiply_security_case_injection(logger):
    # Verifies that the multiply function does not allow injection attacks
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        multiply(2, '3 * 1')
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_power_security_case_injection(logger):
    # Verifies that the power function does not allow injection attacks
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        power(2, '3 ** 1')
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_modulo_security_case_injection(logger):
    # Verifies that the modulo function does not allow injection attacks
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        modulo(10, '3 % 1')
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)

def test_exponential_security_case_injection(logger):
    # Verifies that the exponential function does not allow injection attacks
    logger_handler = logging.StreamHandler(io.StringIO())
    logger.logger.addHandler(logger_handler)
    with pytest.raises(TypeError):
        exponential(2, '3 ** 1')
    logger_handler.close()
    logger.logger.removeHandler(logger_handler)