import pytest
import boto3
from moto import mock_logs, mock_lambda, mock_xray
from psycopg2 import Error as Psycopg2Error
from src.utils.aws_utils import get_cloudwatch_logs, describe_lambda_function, get_xray_traces, connect_to_rds_postgres
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def setup_moto():
    # Mock AWS services
    mock_logs().start()
    mock_lambda().start()
    mock_xray().start()
    yield
    # Clean up
    mock_logs().stop()
    mock_lambda().stop()
    mock_xray().stop()

def test_get_cloudwatch_logs_happy_path(setup_moto):
    # Verify that get_cloudwatch_logs returns log events for a valid log group and log stream
    log_group = 'test-log-group'
    log_stream = 'test-log-stream'
    boto3.client('logs').create_log_group(logGroupName=log_group)
    boto3.client('logs').create_log_stream(logGroupName=log_group, logStreamName=log_stream)
    response = get_cloudwatch_logs(log_group, log_stream)
    assert response is not None

def test_get_cloudwatch_logs_empty_log_group(setup_moto):
    # Verify that get_cloudwatch_logs raises an error for an empty log group
    log_group = ''
    log_stream = 'test-log-stream'
    with pytest.raises(ValueError):
        get_cloudwatch_logs(log_group, log_stream)

def test_get_cloudwatch_logs_empty_log_stream(setup_moto):
    # Verify that get_cloudwatch_logs raises an error for an empty log stream
    log_group = 'test-log-group'
    log_stream = ''
    with pytest.raises(ValueError):
        get_cloudwatch_logs(log_group, log_stream)

def test_describe_lambda_function_happy_path(setup_moto):
    # Verify that describe_lambda_function returns the configuration for a valid lambda function
    function_name = 'test-lambda-function'
    boto3.client('lambda').create_function(FunctionName=function_name, Runtime='python3.8', Role='test-role', Handler='index.handler', Code={'ZipFile': b'bytes'})
    response = describe_lambda_function(function_name)
    assert response is not None

def test_describe_lambda_function_empty_function_name(setup_moto):
    # Verify that describe_lambda_function raises an error for an empty function name
    function_name = ''
    with pytest.raises(ValueError):
        describe_lambda_function(function_name)

def test_get_xray_traces_happy_path(setup_moto):
    # Verify that get_xray_traces returns the service graph for a valid service name
    service_name = 'test-service'
    response = get_xray_traces(service_name)
    assert response is not None

def test_get_xray_traces_empty_service_name(setup_moto):
    # Verify that get_xray_traces raises an error for an empty service name
    service_name = ''
    with pytest.raises(ValueError):
        get_xray_traces(service_name)

def test_connect_to_rds_postgres_happy_path():
    # Verify that connect_to_rds_postgres returns a connection object for valid RDS connection details
    host = 'test-host'
    database = 'test-database'
    user = 'test-user'
    password = 'test-password'
    # Mock the psycopg2 connection
    with pytest.mock.patch('psycopg2.connect') as mock_connect:
        mock_connect.return_value = None
        response = connect_to_rds_postgres(host, database, user, password)
        assert response is None

def test_connect_to_rds_postgres_empty_host():
    # Verify that connect_to_rds_postgres raises an error for an empty host
    host = ''
    database = 'test-database'
    user = 'test-user'
    password = 'test-password'
    with pytest.raises(ValueError):
        connect_to_rds_postgres(host, database, user, password)

def test_connect_to_rds_postgres_empty_database():
    # Verify that connect_to_rds_postgres raises an error for an empty database
    host = 'test-host'
    database = ''
    user = 'test-user'
    password = 'test-password'
    with pytest.raises(ValueError):
        connect_to_rds_postgres(host, database, user, password)

def test_connect_to_rds_postgres_empty_user():
    # Verify that connect_to_rds_postgres raises an error for an empty user
    host = 'test-host'
    database = 'test-database'
    user = ''
    password = 'test-password'
    with pytest.raises(ValueError):
        connect_to_rds_postgres(host, database, user, password)

def test_connect_to_rds_postgres_empty_password():
    # Verify that connect_to_rds_postgres raises an error for an empty password
    host = 'test-host'
    database = 'test-database'
    user = 'test-user'
    password = ''
    with pytest.raises(ValueError):
        connect_to_rds_postgres(host, database, user, password)

def test_connect_to_rds_postgres_invalid_credentials():
    # Verify that connect_to_rds_postgres raises an error for invalid RDS connection details
    host = 'test-host'
    database = 'test-database'
    user = 'test-user'
    password = 'test-password'
    # Mock the psycopg2 connection to raise an error
    with pytest.mock.patch('psycopg2.connect') as mock_connect:
        mock_connect.side_effect = Psycopg2Error('Invalid credentials')
        with pytest.raises(Psycopg2Error):
            connect_to_rds_postgres(host, database, user, password)