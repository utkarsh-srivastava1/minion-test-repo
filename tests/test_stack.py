# tests/test_stack.py
import pytest
from src.stack import Stack

def test_stack_init():
    # Verifies that the stack is initialized with an empty list
    stack = Stack()
    assert stack.items == []

def test_stack_push():
    # Verifies that an item can be pushed onto the stack
    stack = Stack()
    stack.push(1)
    assert stack.items == [1]

def test_stack_push_multiple():
    # Verifies that multiple items can be pushed onto the stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.items == [1, 2, 3]

def test_stack_pop():
    # Verifies that an item can be popped from the stack
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    assert stack.items == []

def test_stack_pop_multiple():
    # Verifies that multiple items can be popped from the stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.items == []

def test_stack_peek():
    # Verifies that the top item can be peeked from the stack
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
    assert stack.items == [1]

def test_stack_is_empty_true():
    # Verifies that is_empty returns True for an empty stack
    stack = Stack()
    assert stack.is_empty() == True

def test_stack_is_empty_false():
    # Verifies that is_empty returns False for a non-empty stack
    stack = Stack()
    stack.push(1)
    assert stack.is_empty() == False

def test_stack_clear():
    # Verifies that the clear method removes all items from the stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.clear()
    assert stack.items == []

def test_stack_pop_empty():
    # Verifies that popping from an empty stack raises an IndexError
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()

def test_stack_peek_empty():
    # Verifies that peeking an empty stack raises an IndexError
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()

def test_stack_push_none():
    # Verifies that pushing None onto the stack does not raise an error
    stack = Stack()
    stack.push(None)
    assert stack.items == [None]

def test_stack_push_multiple_types():
    # Verifies that pushing multiple types onto the stack does not raise an error
    stack = Stack()
    stack.push(1)
    stack.push("hello")
    stack.push(None)
    assert stack.items == [1, "hello", None]

def test_stack_clear_multiple_times():
    # Verifies that clearing the stack multiple times does not raise an error
    stack = Stack()
    stack.clear()
    stack.clear()
    assert stack.items == []

def test_stack_push_and_pop_multiple_times():
    # Verifies that pushing and popping multiple times does not raise an error
    stack = Stack()
    for _ in range(10):
        stack.push(1)
        stack.pop()
    assert stack.items == []