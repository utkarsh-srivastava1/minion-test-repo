from src.utils.aws_utils import get_cloudwatch_logs, describe_lambda_function, get_xray_traces, connect_to_rds_postgres
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_cloudwatch_logs(log_group, log_stream):
    if not log_group or not log_stream:
        logger.error('Invalid log group or log stream')
        raise ValueError('Invalid log group or log stream')
    try:
        logs = get_cloudwatch_logs(log_group, log_stream)
        # Analyze logs for memory usage patterns
        return logs
    except Exception as e:
        logger.error(f'Failed to check cloudwatch logs: {str(e)}')
        raise

def describe_lambda_function_config(function_name):
    if not function_name:
        logger.error('Invalid function name')
        raise ValueError('Invalid function name')
    try:
        config = describe_lambda_function(function_name)
        # Focus on memory settings
        return config
    except Exception as e:
        logger.error(f'Failed to describe lambda function config: {str(e)}')
        raise

def analyze_xray_traces(service_name):
    if not service_name:
        logger.error('Invalid service name')
        raise ValueError('Invalid service name')
    try:
        traces = get_xray_traces(service_name)
        # Detect performance bottlenecks
        return traces
    except Exception as e:
        logger.error(f'Failed to analyze xray traces: {str(e)}')
        raise

def check_rds_postgres(host, database, user, password):
    if not host or not database or not user or not password:
        logger.error('Invalid RDS connection details')
        raise ValueError('Invalid RDS connection details')
    try:
        conn = connect_to_rds_postgres(host, database, user, password)
        # Check for long-running queries or locks
        return conn
    except Exception as e:
        logger.error(f'Failed to check RDS Postgres: {str(e)}')
        raise

def inspect_aws_console(function_name, database):
    if not function_name or not database:
        logger.error('Invalid function name or database')
        raise ValueError('Invalid function name or database')
    try:
        # Inspect AWS Console for recent changes
        return None
    except Exception as e:
        logger.error(f'Failed to inspect AWS Console: {str(e)}')
        raise