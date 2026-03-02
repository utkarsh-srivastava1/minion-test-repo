import pytest
import logging
import json
import os
from src.logger import Logger

# Setup and teardown
@pytest.fixture
def logger():
    yield Logger('test_logger')
    # Remove log files after test
    if os.path.exists('app.log'):
        os.remove('app.log')
    if os.path.exists('error.log'):
        os.remove('error.log')
    if os.path.exists('logging_config.json'):
        os.remove('logging_config.json')

# Happy path
def test_logger_init(logger):
    # Verify logger is initialized with default config
    assert logger.logger.level == logging.DEBUG
    assert logger.handler.level == logging.DEBUG
    assert logger.stream_handler.level == logging.DEBUG
    assert logger.error_handler.level == logging.ERROR

def test_logger_debug(logger):
    # Verify debug message is logged
    logger.debug('Test debug message')
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'DEBUG' in log_message

def test_logger_info(logger):
    # Verify info message is logged
    logger.info('Test info message')
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'INFO' in log_message

def test_logger_warning(logger):
    # Verify warning message is logged
    logger.warning('Test warning message')
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'WARNING' in log_message

def test_logger_error(logger):
    # Verify error message is logged
    logger.error('Test error message')
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'ERROR' in log_message
    with open('error.log', 'r') as f:
        error_log_message = f.read()
    assert 'ERROR' in error_log_message

def test_logger_critical(logger):
    # Verify critical message is logged
    logger.critical('Test critical message')
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'CRITICAL' in log_message

# Edge cases
def test_logger_empty_message(logger):
    # Verify empty message is logged
    logger.debug('')
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'DEBUG' in log_message

def test_logger_none_message(logger):
    # Verify None message is logged
    logger.debug(None)
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'DEBUG' in log_message

# Error cases
def test_logger_invalid_config():
    # Verify invalid config raises exception
    with open('logging_config.json', 'w') as f:
        json.dump({'level': 'INVALID'}, f)
    with pytest.raises(KeyError):
        Logger('test_logger')

def test_logger_config_file_not_found():
    # Verify config file not found uses default config
    logger = Logger('test_logger')
    assert logger.logger.level == logging.DEBUG

def test_logger_invalid_log_level():
    # Verify invalid log level raises exception
    with open('logging_config.json', 'w') as f:
        json.dump({'level': 'INVALID'}, f)
    with pytest.raises(ValueError):
        Logger('test_logger')

# Security cases
def test_logger_injection(logger):
    # Verify injection attack is prevented
    logger.debug('Test debug message %s', 'injection')
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'injection' in log_message

def test_logger_malformed_data(logger):
    # Verify malformed data is handled
    logger.debug('Test debug message %s', None)
    with open('app.log', 'r') as f:
        log_message = f.read()
    assert 'DEBUG' in log_message