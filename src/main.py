from src.logger import Logger

def hello() -> str:
    logger = Logger(__name__)
    logger.info('Hello function called')
    return 'Hello World'

def add(a: float, b: float) -> float:
    logger = Logger(__name__)
    logger.info('Add function called')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        logger.error('Both inputs must be numbers')
        raise TypeError('Both inputs must be numbers')
    try:
        result = a + b
        if result == float('inf') or result == float('-inf'):
            logger.error('Result is too large')
            raise OverflowError('Result is too large')
        logger.info(f'Result: {result}')
        return result
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        raise ValueError(f'An error occurred: {str(e)}')

def multiply(a: float, b: float) -> float:
    logger = Logger(__name__)
    logger.info('Multiply function called')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        logger.error('Both inputs must be numbers')
        raise TypeError('Both inputs must be numbers')
    try:
        result = a * b
        if result == float('inf') or result == float('-inf'):
            logger.error('Result is too large')
            raise OverflowError('Result is too large')
        logger.info(f'Result: {result}')
        return result
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        raise ValueError(f'An error occurred: {str(e)}')

def power(x: float, y: float) -> float:
    logger = Logger(__name__)
    logger.info('Power function called')
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        logger.error('Both inputs must be numbers')
        raise TypeError('Both inputs must be numbers')
    try:
        result = x ** y
        if result == float('inf') or result == float('-inf'):
            logger.error('Result is too large')
            raise OverflowError('Result is too large')
        logger.info(f'Result: {result}')
        return result
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        raise ValueError(f'An error occurred: {str(e)}')

def modulo(x: float, y: float) -> float:
    logger = Logger(__name__)
    logger.info('Modulo function called')
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        logger.error('Both inputs must be numbers')
        raise TypeError('Both inputs must be numbers')
    if y == 0:
        logger.error('Cannot divide by zero')
        raise ZeroDivisionError('Cannot divide by zero')
    try:
        result = x % y
        logger.info(f'Result: {result}')
        return result
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        raise ValueError(f'An error occurred: {str(e)}')

def exponential(n: float, exponent: int) -> float:
    logger = Logger(__name__)
    logger.info('Exponential function called')
    if not isinstance(n, (int, float)) or not isinstance(exponent, int):
        logger.error('Base must be a number and exponent must be an integer')
        raise TypeError('Base must be a number and exponent must be an integer')
    if exponent == 0:
        logger.info('Result: 1')
        return 1
    elif exponent < 0:
        logger.info('Calculating reciprocal')
        return 1 / exponential(n, -exponent)
    elif exponent % 2 == 0:
        logger.info('Calculating half power')
        half_pow = exponential(n, exponent // 2)
        logger.info(f'Result: {half_pow * half_pow}')
        return half_pow * half_pow
    else:
        logger.info('Calculating half power and multiplying by base')
        half_pow = exponential(n, (exponent - 1) // 2)
        logger.info(f'Result: {n * half_pow * half_pow}')
        return n * half_pow * half_pow
