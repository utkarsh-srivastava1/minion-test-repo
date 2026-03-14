# tests/test_binary_tree.py

import pytest
from src.binary_tree import BinaryTree, Node

@pytest.fixture
def binary_tree():
    """Setup a binary tree instance for testing"""
    return BinaryTree()

def test_insert_and_search_happy_path(binary_tree):
    # Verify that insert and search work as expected for normal values
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    assert binary_tree.search(5) is True
    assert binary_tree.search(3) is True
    assert binary_tree.search(7) is True
    assert binary_tree.search(9) is False

def test_insert_empty_tree(binary_tree):
    # Verify that inserting into an empty tree works as expected
    assert binary_tree.root is None
    binary_tree.insert(5)
    assert binary_tree.root.value == 5
    assert binary_tree.root.left is None
    assert binary_tree.root.right is None

def test_insert_duplicate_value(binary_tree):
    # Verify that inserting a duplicate value does not create a new node
    binary_tree.insert(5)
    binary_tree.insert(5)
    assert binary_tree.root.value == 5
    assert binary_tree.root.left is None
    assert binary_tree.root.right is None

def test_search_empty_tree(binary_tree):
    # Verify that searching an empty tree returns False
    assert binary_tree.search(5) is False

def test_search_non_existent_value(binary_tree):
    # Verify that searching for a non-existent value returns False
    binary_tree.insert(5)
    assert binary_tree.search(3) is False

def test_insert_none_value(binary_tree):
    # Verify that inserting a None value raises an error
    with pytest.raises(TypeError):
        binary_tree.insert(None)

def test_search_none_value(binary_tree):
    # Verify that searching for a None value raises an error
    with pytest.raises(TypeError):
        binary_tree.search(None)

def test_insert_non_numeric_value(binary_tree):
    # Verify that inserting a non-numeric value raises an error
    with pytest.raises(TypeError):
        binary_tree.insert("five")

def test_search_non_numeric_value(binary_tree):
    # Verify that searching for a non-numeric value raises an error
    with pytest.raises(TypeError):
        binary_tree.search("five")

def test_insert_large_values(binary_tree):
    # Verify that inserting large values works as expected
    binary_tree.insert(1000)
    binary_tree.insert(2000)
    assert binary_tree.search(1000) is True
    assert binary_tree.search(2000) is True

def test_insert_negative_values(binary_tree):
    # Verify that inserting negative values works as expected
    binary_tree.insert(-5)
    binary_tree.insert(-10)
    assert binary_tree.search(-5) is True
    assert binary_tree.search(-10) is True

def test_insert_float_values(binary_tree):
    # Verify that inserting float values works as expected
    binary_tree.insert(5.5)
    binary_tree.insert(3.3)
    assert binary_tree.search(5.5) is True
    assert binary_tree.search(3.3) is True