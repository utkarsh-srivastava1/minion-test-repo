# tests/test_main.py
import pytest
from flask.testing import FlaskClient
from src.main import app, add, multiply, power, modulo, divide
import json

@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_hello_function():
    # Test the hello function
    assert 'Hello World' == 'Hello World'

def test_add_function_happy_path():
    # Test the add function with valid inputs
    assert add(2, 3) == 5

def test_add_function_edge_case_empty_inputs():
    # Test the add function with empty inputs
    with pytest.raises(TypeError):
        add(None, 3)

def test_add_function_edge_case_boundary_values():
    # Test the add function with boundary values
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_add_function_error_case_invalid_inputs():
    # Test the add function with invalid inputs
    with pytest.raises(TypeError):
        add('a', 3)

def test_multiply_function_happy_path():
    # Test the multiply function with valid inputs
    assert multiply(2, 3) == 6

def test_multiply_function_edge_case_empty_inputs():
    # Test the multiply function with empty inputs
    with pytest.raises(TypeError):
        multiply(None, 3)

def test_multiply_function_edge_case_boundary_values():
    # Test the multiply function with boundary values
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1

def test_multiply_function_error_case_invalid_inputs():
    # Test the multiply function with invalid inputs
    with pytest.raises(TypeError):
        multiply('a', 3)

def test_power_function_happy_path():
    # Test the power function with valid inputs
    assert power(2, 3) == 8

def test_power_function_edge_case_empty_inputs():
    # Test the power function with empty inputs
    with pytest.raises(TypeError):
        power(None, 3)

def test_power_function_edge_case_boundary_values():
    # Test the power function with boundary values
    assert power(0, 0) == 1
    assert power(-1, 1) == -1

def test_power_function_error_case_invalid_inputs():
    # Test the power function with invalid inputs
    with pytest.raises(TypeError):
        power('a', 3)

def test_modulo_function_happy_path():
    # Test the modulo function with valid inputs
    assert modulo(10, 3) == 1

def test_modulo_function_edge_case_empty_inputs():
    # Test the modulo function with empty inputs
    with pytest.raises(TypeError):
        modulo(None, 3)

def test_modulo_function_edge_case_boundary_values():
    # Test the modulo function with boundary values
    assert modulo(0, 1) == 0
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)

def test_modulo_function_error_case_invalid_inputs():
    # Test the modulo function with invalid inputs
    with pytest.raises(TypeError):
        modulo('a', 3)

def test_divide_function_happy_path():
    # Test the divide function with valid inputs
    assert divide(10, 2) == 5

def test_divide_function_edge_case_empty_inputs():
    # Test the divide function with empty inputs
    with pytest.raises(TypeError):
        divide(None, 3)

def test_divide_function_edge_case_boundary_values():
    # Test the divide function with boundary values
    assert divide(0, 1) == 0
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_function_error_case_invalid_inputs():
    # Test the divide function with invalid inputs
    with pytest.raises(TypeError):
        divide('a', 3)

def test_index_route_get_request(client):
    # Test the index route with a GET request
    response = client.get('/')
    assert response.status_code == 200

def test_index_route_post_request_valid_inputs(client):
    # Test the index route with a POST request and valid inputs
    response = client.post('/', data={'a': 2, 'b': 3, 'operation': 'add'})
    assert response.status_code == 200
    assert json.loads(response.data)['result'] == 5

def test_index_route_post_request_invalid_inputs(client):
    # Test the index route with a POST request and invalid inputs
    response = client.post('/', data={'a': 'a', 'b': 3, 'operation': 'add'})
    assert response.status_code == 200
    assert 'Both inputs must be numbers' in response.data.decode('utf-8')

def test_index_route_post_request_invalid_operation(client):
    # Test the index route with a POST request and an invalid operation
    response = client.post('/', data={'a': 2, 'b': 3, 'operation': 'invalid'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Invalid operation'

def test_index_route_post_request_division_by_zero(client):
    # Test the index route with a POST request and division by zero
    response = client.post('/', data={'a': 10, 'b': 0, 'operation': 'divide'})
    assert response.status_code == 200
    assert 'Cannot divide by zero' in response.data.decode('utf-8')