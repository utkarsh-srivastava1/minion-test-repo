# tests/test_stack.py
import pytest
from src.stack import Stack
from unittest.mock import patch
from io import StringIO
import sys

@pytest.fixture
def stack():
    # Setup: Create a new stack instance
    return Stack()

def test_stack_init(stack):
    # Verifies: Stack is initialized with an empty list and a logger
    assert stack.items == []
    assert hasattr(stack, 'logger')

def test_push_happy_path(stack):
    # Verifies: Pushing an item to the stack adds it to the list
    item = 'test_item'
    stack.push(item)
    assert stack.items == [item]

def test_push_edge_case_empty_string(stack):
    # Verifies: Pushing an empty string to the stack adds it to the list
    item = ''
    stack.push(item)
    assert stack.items == [item]

def test_push_edge_case_none_value(stack):
    # Verifies: Pushing None to the stack adds it to the list
    item = None
    stack.push(item)
    assert stack.items == [item]

def test_pop_happy_path(stack):
    # Verifies: Popping an item from the stack removes it from the list
    item = 'test_item'
    stack.push(item)
    popped_item = stack.pop()
    assert popped_item == item
    assert stack.items == []

def test_pop_edge_case_empty_stack(stack):
    # Verifies: Popping from an empty stack raises an IndexError
    with pytest.raises(IndexError):
        stack.pop()

def test_peek_happy_path(stack):
    # Verifies: Peeking an item from the stack returns the top item
    item = 'test_item'
    stack.push(item)
    peeked_item = stack.peek()
    assert peeked_item == item
    assert stack.items == [item]

def test_peek_edge_case_empty_stack(stack):
    # Verifies: Peeking an empty stack raises an IndexError
    with pytest.raises(IndexError):
        stack.peek()

def test_is_empty_happy_path(stack):
    # Verifies: Checking if the stack is empty returns True for an empty stack
    assert stack.is_empty()

def test_is_empty_happy_path_non_empty(stack):
    # Verifies: Checking if the stack is empty returns False for a non-empty stack
    item = 'test_item'
    stack.push(item)
    assert not stack.is_empty()

def test_clear_happy_path(stack):
    # Verifies: Clearing the stack removes all items
    item = 'test_item'
    stack.push(item)
    stack.clear()
    assert stack.items == []

def test_clear_edge_case_empty_stack(stack):
    # Verifies: Clearing an empty stack does not raise any errors
    stack.clear()
    assert stack.items == []

@patch('sys.stdout', new_callable=StringIO)
def test_push_logs_info(mock_stdout, stack):
    # Verifies: Pushing an item logs an info message
    item = 'test_item'
    stack.push(item)
    assert f'Pushing item: {item}' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_pop_logs_info(mock_stdout, stack):
    # Verifies: Popping an item logs an info message
    item = 'test_item'
    stack.push(item)
    stack.pop()
    assert 'Popping item' in mock_stdout.getvalue()
    assert f'Popped item: {item}' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_peek_logs_info(mock_stdout, stack):
    # Verifies: Peeking an item logs an info message
    item = 'test_item'
    stack.push(item)
    stack.peek()
    assert 'Peeking item' in mock_stdout.getvalue()
    assert f'Peeked item: {item}' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_is_empty_logs_info(mock_stdout, stack):
    # Verifies: Checking if the stack is empty logs an info message
    stack.is_empty()
    assert 'Checking if stack is empty' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_clear_logs_info(mock_stdout, stack):
    # Verifies: Clearing the stack logs an info message
    stack.clear()
    assert 'Clearing stack' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_pop_logs_error(mock_stdout, stack):
    # Verifies: Popping from an empty stack logs an error message
    with pytest.raises(IndexError):
        stack.pop()
    assert 'Stack is empty' in mock_stdout.getvalue()

@patch('sys.stdout', new_callable=StringIO)
def test_peek_logs_error(mock_stdout, stack):
    # Verifies: Peeking an empty stack logs an error message
    with pytest.raises(IndexError):
        stack.peek()
    assert 'Stack is empty' in mock_stdout.getvalue()