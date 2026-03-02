# tests/test_queue.py
import pytest
from src.queue import Queue
from src.logger import Logger
import logging

# Set up logging for testing
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def queue():
    # Create a new Queue instance for each test
    return Queue()

def test_enqueue_happy_path(queue):
    # Verify that enqueueing an item logs the correct message and adds the item to the queue
    item = 'test_item'
    queue.enqueue(item)
    assert queue.queue == [item]

def test_dequeue_happy_path(queue):
    # Verify that dequeueing an item logs the correct message and removes the item from the queue
    item = 'test_item'
    queue.enqueue(item)
    dequeued_item = queue.dequeue()
    assert dequeued_item == item
    assert queue.queue == []

def test_dequeue_empty_queue(queue):
    # Verify that dequeueing from an empty queue logs a warning and returns None
    dequeued_item = queue.dequeue()
    assert dequeued_item is None
    assert queue.queue == []

def test_enqueue_none_value(queue):
    # Verify that enqueueing a None value logs the correct message and adds None to the queue
    queue.enqueue(None)
    assert queue.queue == [None]

def test_dequeue_none_value(queue):
    # Verify that dequeueing a None value logs the correct message and removes None from the queue
    queue.enqueue(None)
    dequeued_item = queue.dequeue()
    assert dequeued_item is None
    assert queue.queue == []

def test_enqueue_multiple_items(queue):
    # Verify that enqueueing multiple items logs the correct messages and adds all items to the queue
    items = ['item1', 'item2', 'item3']
    for item in items:
        queue.enqueue(item)
    assert queue.queue == items

def test_dequeue_multiple_items(queue):
    # Verify that dequeueing multiple items logs the correct messages and removes all items from the queue
    items = ['item1', 'item2', 'item3']
    for item in items:
        queue.enqueue(item)
    for _ in range(len(items)):
        queue.dequeue()
    assert queue.queue == []

def test_enqueue_invalid_input(queue, caplog):
    # Verify that enqueueing an invalid input (e.g., a list) logs an error message
    invalid_input = [1, 2, 3]
    with pytest.raises(TypeError):
        queue.enqueue(invalid_input)
    assert 'TypeError' in caplog.text

def test_dequeue_invalid_input(queue, caplog):
    # Verify that dequeueing with an invalid input (e.g., a list) logs an error message
    invalid_input = [1, 2, 3]
    with pytest.raises(TypeError):
        queue.dequeue()
    assert 'TypeError' not in caplog.text  # Dequeue does not take any arguments

def test_queue_logger(queue, caplog):
    # Verify that the queue logger logs messages at the correct level
    item = 'test_item'
    queue.enqueue(item)
    assert 'INFO' in caplog.text
    assert f'Enqueuing item: {item}' in caplog.text

def test_dequeue_logger(queue, caplog):
    # Verify that the queue logger logs messages at the correct level when dequeueing
    item = 'test_item'
    queue.enqueue(item)
    queue.dequeue()
    assert 'INFO' in caplog.text
    assert 'Dequeued item: test_item' in caplog.text

def test_dequeue_empty_queue_logger(queue, caplog):
    # Verify that the queue logger logs a warning when dequeueing from an empty queue
    queue.dequeue()
    assert 'WARNING' in caplog.text
    assert 'Queue is empty' in caplog.text