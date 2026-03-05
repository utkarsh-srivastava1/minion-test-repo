import boto3
import json
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_cloudwatch_logs(log_group, log_stream):
    if not log_group or not log_stream:
        logger.error('Invalid log group or log stream')
        raise ValueError('Invalid log group or log stream')
    try:
        session = boto3.Session()
        client = session.client('logs')
        response = client.get_log_events(logGroupName=log_group, logStreamName=log_stream)
        return response['events']
    except Exception as e:
        if 'ThrottlingException' in str(e):
            logger.error(f'Throttling exception occurred while getting cloudwatch logs: {str(e)}')
            # Implement retry logic or exponential backoff
            raise
        logger.error(f'Failed to get cloudwatch logs: {str(e)}')
        raise

def describe_lambda_function(function_name):
    if not function_name:
        logger.error('Invalid function name')
        raise ValueError('Invalid function name')
    try:
        session = boto3.Session()
        client = session.client('lambda')
        response = client.get_function_configuration(FunctionName=function_name)
        return response
    except Exception as e:
        if 'ThrottlingException' in str(e):
            logger.error(f'Throttling exception occurred while describing lambda function: {str(e)}')
            # Implement retry logic or exponential backoff
            raise
        logger.error(f'Failed to describe lambda function: {str(e)}')
        raise

def get_xray_traces(service_name):
    if not service_name:
        logger.error('Invalid service name')
        raise ValueError('Invalid service name')
    try:
        session = boto3.Session()
        client = session.client('xray')
        response = client.get_service_graph(StartTime='1h ago', EndTime='now', ServiceNames=[service_name])
        return response
    except Exception as e:
        if 'ThrottlingException' in str(e):
            logger.error(f'Throttling exception occurred while getting xray traces: {str(e)}')
            # Implement retry logic or exponential backoff
            raise
        logger.error(f'Failed to get xray traces: {str(e)}')
        raise

def connect_to_rds_postgres(host, database, user, password):
    if not host or not database or not user or not password:
        logger.error('Invalid RDS connection details')
        raise ValueError('Invalid RDS connection details')
    try:
        import psycopg2
        conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        return conn
    except Exception as e:
        logger.error(f'Failed to connect to RDS Postgres: {str(e)}')
        raise