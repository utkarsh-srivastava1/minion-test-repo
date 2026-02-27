# tests/test_linked_list.py

import pytest
from src.linked_list import LinkedList, Node

def test_linked_list_append_happy_path():
    # Verifies that append method adds elements to the end of the list
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    current = linked_list.head
    expected = [1, 2, 3]
    index = 0
    while current:
        assert current.data == expected[index]
        current = current.next
        index += 1

def test_linked_list_remove_happy_path():
    # Verifies that remove method removes the first occurrence of the specified element
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.remove(2)
    current = linked_list.head
    expected = [1, 3]
    index = 0
    while current:
        assert current.data == expected[index]
        current = current.next
        index += 1

def test_linked_list_append_empty_list():
    # Verifies that append method works correctly with an empty list
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.head.data == 1

def test_linked_list_remove_empty_list():
    # Verifies that remove method does not throw an error with an empty list
    linked_list = LinkedList()
    linked_list.remove(1)
    assert linked_list.head is None

def test_linked_list_append_none_value():
    # Verifies that append method works correctly with a None value
    linked_list = LinkedList()
    linked_list.append(None)
    assert linked_list.head.data is None

def test_linked_list_remove_none_value():
    # Verifies that remove method works correctly with a None value
    linked_list = LinkedList()
    linked_list.append(None)
    linked_list.remove(None)
    assert linked_list.head is None

def test_linked_list_append_multiple_none_values():
    # Verifies that append method works correctly with multiple None values
    linked_list = LinkedList()
    linked_list.append(None)
    linked_list.append(None)
    linked_list.append(None)
    current = linked_list.head
    expected = [None, None, None]
    index = 0
    while current:
        assert current.data == expected[index]
        current = current.next
        index += 1

def test_linked_list_remove_multiple_none_values():
    # Verifies that remove method works correctly with multiple None values
    linked_list = LinkedList()
    linked_list.append(None)
    linked_list.append(None)
    linked_list.append(None)
    linked_list.remove(None)
    current = linked_list.head
    expected = [None, None]
    index = 0
    while current:
        assert current.data == expected[index]
        current = current.next
        index += 1

def test_linked_list_remove_non_existent_value():
    # Verifies that remove method does not throw an error with a non-existent value
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.remove(3)
    current = linked_list.head
    expected = [1, 2]
    index = 0
    while current:
        assert current.data == expected[index]
        current = current.next
        index += 1

def test_linked_list_remove_head():
    # Verifies that remove method works correctly when removing the head of the list
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.remove(1)
    assert linked_list.head.data == 2

def test_linked_list_remove_tail():
    # Verifies that remove method works correctly when removing the tail of the list
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.remove(2)
    assert linked_list.head.data == 1
    assert linked_list.head.next is None

def test_linked_list_remove_all():
    # Verifies that remove method works correctly when removing all elements from the list
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(1)
    linked_list.append(1)
    linked_list.remove(1)
    linked_list.remove(1)
    linked_list.remove(1)
    assert linked_list.head is None

def test_linked_list_append_and_remove_multiple_times():
    # Verifies that append and remove methods work correctly when called multiple times
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.remove(1)
    linked_list.append(3)
    linked_list.remove(2)
    linked_list.append(4)
    linked_list.remove(3)
    linked_list.append(5)
    linked_list.remove(4)
    assert linked_list.head.data == 5
    assert linked_list.head.next is None