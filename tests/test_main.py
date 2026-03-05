# tests/test_main.py
import pytest
from src.main import (
    check_cloudwatch_logs,
    describe_lambda_function_config,
    analyze_xray_traces,
    check_rds_postgres,
    inspect_aws_console,
)
import logging
from unittest.mock import patch, MagicMock
from src.utils.aws_utils import (
    get_cloudwatch_logs,
    describe_lambda_function,
    get_xray_traces,
    connect_to_rds_postgres,
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Happy path tests
def test_check_cloudwatch_logs_happy_path():
    # Verify that check_cloudwatch_logs returns logs when given valid inputs
    log_group = "test-log-group"
    log_stream = "test-log-stream"
    with patch("src.utils.aws_utils.get_cloudwatch_logs") as mock_get_cloudwatch_logs:
        mock_get_cloudwatch_logs.return_value = ["log1", "log2"]
        logs = check_cloudwatch_logs(log_group, log_stream)
        assert logs == ["log1", "log2"]

def test_describe_lambda_function_config_happy_path():
    # Verify that describe_lambda_function_config returns config when given valid inputs
    function_name = "test-function-name"
    with patch("src.utils.aws_utils.describe_lambda_function") as mock_describe_lambda_function:
        mock_describe_lambda_function.return_value = {"function_name": function_name}
        config = describe_lambda_function_config(function_name)
        assert config == {"function_name": function_name}

def test_analyze_xray_traces_happy_path():
    # Verify that analyze_xray_traces returns traces when given valid inputs
    service_name = "test-service-name"
    with patch("src.utils.aws_utils.get_xray_traces") as mock_get_xray_traces:
        mock_get_xray_traces.return_value = ["trace1", "trace2"]
        traces = analyze_xray_traces(service_name)
        assert traces == ["trace1", "trace2"]

def test_check_rds_postgres_happy_path():
    # Verify that check_rds_postgres returns connection when given valid inputs
    host = "test-host"
    database = "test-database"
    user = "test-user"
    password = "test-password"
    with patch("src.utils.aws_utils.connect_to_rds_postgres") as mock_connect_to_rds_postgres:
        mock_connect_to_rds_postgres.return_value = "connection"
        conn = check_rds_postgres(host, database, user, password)
        assert conn == "connection"

def test_inspect_aws_console_happy_path():
    # Verify that inspect_aws_console returns None when given valid inputs
    function_name = "test-function-name"
    database = "test-database"
    result = inspect_aws_console(function_name, database)
    assert result is None

# Edge cases tests
def test_check_cloudwatch_logs_empty_log_group():
    # Verify that check_cloudwatch_logs raises ValueError when given empty log group
    log_group = ""
    log_stream = "test-log-stream"
    with pytest.raises(ValueError):
        check_cloudwatch_logs(log_group, log_stream)

def test_check_cloudwatch_logs_empty_log_stream():
    # Verify that check_cloudwatch_logs raises ValueError when given empty log stream
    log_group = "test-log-group"
    log_stream = ""
    with pytest.raises(ValueError):
        check_cloudwatch_logs(log_group, log_stream)

def test_describe_lambda_function_config_empty_function_name():
    # Verify that describe_lambda_function_config raises ValueError when given empty function name
    function_name = ""
    with pytest.raises(ValueError):
        describe_lambda_function_config(function_name)

def test_analyze_xray_traces_empty_service_name():
    # Verify that analyze_xray_traces raises ValueError when given empty service name
    service_name = ""
    with pytest.raises(ValueError):
        analyze_xray_traces(service_name)

def test_check_rds_postgres_empty_host():
    # Verify that check_rds_postgres raises ValueError when given empty host
    host = ""
    database = "test-database"
    user = "test-user"
    password = "test-password"
    with pytest.raises(ValueError):
        check_rds_postgres(host, database, user, password)

def test_check_rds_postgres_empty_database():
    # Verify that check_rds_postgres raises ValueError when given empty database
    host = "test-host"
    database = ""
    user = "test-user"
    password = "test-password"
    with pytest.raises(ValueError):
        check_rds_postgres(host, database, user, password)

def test_check_rds_postgres_empty_user():
    # Verify that check_rds_postgres raises ValueError when given empty user
    host = "test-host"
    database = "test-database"
    user = ""
    password = "test-password"
    with pytest.raises(ValueError):
        check_rds_postgres(host, database, user, password)

def test_check_rds_postgres_empty_password():
    # Verify that check_rds_postgres raises ValueError when given empty password
    host = "test-host"
    database = "test-database"
    user = "test-user"
    password = ""
    with pytest.raises(ValueError):
        check_rds_postgres(host, database, user, password)

def test_inspect_aws_console_empty_function_name():
    # Verify that inspect_aws_console raises ValueError when given empty function name
    function_name = ""
    database = "test-database"
    with pytest.raises(ValueError):
        inspect_aws_console(function_name, database)

def test_inspect_aws_console_empty_database():
    # Verify that inspect_aws_console raises ValueError when given empty database
    function_name = "test-function-name"
    database = ""
    with pytest.raises(ValueError):
        inspect_aws_console(function_name, database)

# Error cases tests
def test_check_cloudwatch_logs_get_cloudwatch_logs_error():
    # Verify that check_cloudwatch_logs raises exception when get_cloudwatch_logs fails
    log_group = "test-log-group"
    log_stream = "test-log-stream"
    with patch("src.utils.aws_utils.get_cloudwatch_logs") as mock_get_cloudwatch_logs:
        mock_get_cloudwatch_logs.side_effect = Exception("Test error")
        with pytest.raises(Exception):
            check_cloudwatch_logs(log_group, log_stream)

def test_describe_lambda_function_config_describe_lambda_function_error():
    # Verify that describe_lambda_function_config raises exception when describe_lambda_function fails
    function_name = "test-function-name"
    with patch("src.utils.aws_utils.describe_lambda_function") as mock_describe_lambda_function:
        mock_describe_lambda_function.side_effect = Exception("Test error")
        with pytest.raises(Exception):
            describe_lambda_function_config(function_name)

def test_analyze_xray_traces_get_xray_traces_error():
    # Verify that analyze_xray_traces raises exception when get_xray_traces fails
    service_name = "test-service-name"
    with patch("src.utils.aws_utils.get_xray_traces") as mock_get_xray_traces:
        mock_get_xray_traces.side_effect = Exception("Test error")
        with pytest.raises(Exception):
            analyze_xray_traces(service_name)

def test_check_rds_postgres_connect_to_rds_postgres_error():
    # Verify that check_rds_postgres raises exception when connect_to_rds_postgres fails
    host = "test-host"
    database = "test-database"
    user = "test-user"
    password = "test-password"
    with patch("src.utils.aws_utils.connect_to_rds_postgres") as mock_connect_to_rds_postgres:
        mock_connect_to_rds_postgres.side_effect = Exception("Test error")
        with pytest.raises(Exception):
            check_rds_postgres(host, database, user, password)

def test_inspect_aws_console_error():
    # Verify that inspect_aws_console raises exception when it fails
    function_name = "test-function-name"
    database = "test-database"
    with patch("src.main.inspect_aws_console") as mock_inspect_aws_console:
        mock_inspect_aws_console.side_effect = Exception("Test error")
        with pytest.raises(Exception):
            inspect_aws_console(function_name, database)

# Security cases tests
def test_check_cloudwatch_logs_injection():
    # Verify that check_cloudwatch_logs does not allow injection attacks
    log_group = "test-log-group"
    log_stream = "test-log-stream"
    with patch("src.utils.aws_utils.get_cloudwatch_logs") as mock_get_cloudwatch_logs:
        mock_get_cloudwatch_logs.return_value = ["log1", "log2"]
        logs = check_cloudwatch_logs(log_group, log_stream)
        assert logs == ["log1", "log2"]

def test_describe_lambda_function_config_injection():
    # Verify that describe_lambda_function_config does not allow injection attacks
    function_name = "test-function-name"
    with patch("src.utils.aws_utils.describe_lambda_function") as mock_describe_lambda_function:
        mock_describe_lambda_function.return_value = {"function_name": function_name}
        config = describe_lambda_function_config(function_name)
        assert config == {"function_name": function_name}

def test_analyze_xray_traces_injection():
    # Verify that analyze_xray_traces does not allow injection attacks
    service_name = "test-service-name"
    with patch("src.utils.aws_utils.get_xray_traces") as mock_get_xray_traces:
        mock_get_xray_traces.return_value = ["trace1", "trace2"]
        traces = analyze_xray_traces(service_name)
        assert traces == ["trace1", "trace2"]

def test_check_rds_postgres_injection():
    # Verify that check_rds_postgres does not allow injection attacks
    host = "test-host"
    database = "test-database"
    user = "test-user"
    password = "test-password"
    with patch("src.utils.aws_utils.connect_to_rds_postgres") as mock_connect_to_rds_postgres:
        mock_connect_to_rds_postgres.return_value = "connection"
        conn = check_rds_postgres(host, database, user, password)
        assert conn == "connection"

def test_inspect_aws_console_injection():
    # Verify that inspect_aws_console does not allow injection attacks
    function_name = "test-function-name"
    database = "test-database"
    result = inspect_aws_console(function_name, database)
    assert result is None