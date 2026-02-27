def hello() -> str:
    return 'Hello World'


def add(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    try:
        result = a + b
        if result == float('inf') or result == float('-inf'):
            raise OverflowError('Result is too large')
        return result
    except Exception as e:
        raise ValueError(f'An error occurred: {str(e)}')


def multiply(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    try:
        result = a * b
        if result == float('inf') or result == float('-inf'):
            raise OverflowError('Result is too large')
        return result
    except Exception as e:
        raise ValueError(f'An error occurred: {str(e)}')


def power(x: float, y: float) -> float:
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError('Both inputs must be numbers')
    try:
        result = x ** y
        if result == float('inf') or result == float('-inf'):
            raise OverflowError('Result is too large')
        return result
    except Exception as e:
        raise ValueError(f'An error occurred: {str(e)}')
