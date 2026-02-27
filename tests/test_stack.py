# tests/test_stack.py

import pytest
from src.stack import Stack

@pytest.fixture
def empty_stack():
    """Setup an empty stack for testing"""
    return Stack()

@pytest.fixture
def populated_stack():
    """Setup a populated stack for testing"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

def test_stack_init(empty_stack):
    # Verify that the stack is initialized with an empty list
    assert empty_stack.items == []

def test_push_pop_empty_stack(empty_stack):
    # Verify that pushing and popping an item from an empty stack works as expected
    empty_stack.push(1)
    assert empty_stack.pop() == 1

def test_push_pop_populated_stack(populated_stack):
    # Verify that pushing and popping items from a populated stack works as expected
    assert populated_stack.pop() == 3
    assert populated_stack.pop() == 2
    assert populated_stack.pop() == 1

def test_peek_empty_stack(empty_stack):
    # Verify that peeking an empty stack raises an IndexError
    with pytest.raises(IndexError):
        empty_stack.peek()

def test_peek_populated_stack(populated_stack):
    # Verify that peeking a populated stack returns the top item
    assert populated_stack.peek() == 3

def test_is_empty_empty_stack(empty_stack):
    # Verify that is_empty returns True for an empty stack
    assert empty_stack.is_empty()

def test_is_empty_populated_stack(populated_stack):
    # Verify that is_empty returns False for a populated stack
    assert not populated_stack.is_empty()

def test_push_multiple_items(populated_stack):
    # Verify that pushing multiple items works as expected
    populated_stack.push(4)
    populated_stack.push(5)
    assert populated_stack.pop() == 5
    assert populated_stack.pop() == 4

def test_pop_from_empty_stack(empty_stack):
    # Verify that popping from an empty stack raises an IndexError
    with pytest.raises(IndexError):
        empty_stack.pop()

def test_peek_empty_stack_error(empty_stack):
    # Verify that peeking an empty stack raises an IndexError with the correct message
    with pytest.raises(IndexError) as e:
        empty_stack.peek()
    assert str(e.value) == 'Cannot peek an empty stack'

def test_pop_empty_stack_error(empty_stack):
    # Verify that popping an empty stack raises an IndexError with the correct message
    with pytest.raises(IndexError) as e:
        empty_stack.pop()
    assert str(e.value) == 'Cannot pop from an empty stack'

def test_push_none_value(empty_stack):
    # Verify that pushing a None value works as expected
    empty_stack.push(None)
    assert empty_stack.pop() is None

def test_push_malformed_data(empty_stack):
    # Verify that pushing malformed data (e.g., a list) works as expected
    empty_stack.push([1, 2, 3])
    assert empty_stack.pop() == [1, 2, 3]