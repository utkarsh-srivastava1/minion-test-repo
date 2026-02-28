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


def modulo(x: float, y: float) -> float:
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError('Both inputs must be numbers')
    if y == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    try:
        result = x % y
        return result
    except Exception as e:
        raise ValueError(f'An error occurred: {str(e)}')


def exponential(n: float, exponent: int) -> float:
    if not isinstance(n, (int, float)) or not isinstance(exponent, int):
        raise TypeError('Base must be a number and exponent must be an integer')
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / exponential(n, -exponent)
    elif exponent % 2 == 0:
        half_pow = exponential(n, exponent // 2)
        return half_pow * half_pow
    else:
        half_pow = exponential(n, (exponent - 1) // 2)
        return n * half_pow * half_pow


def square_root(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError('Input must be a number')
    if x < 0:
        raise ValueError('Cannot calculate square root of negative number')
    try:
        result = x ** 0.5
        return result
    except Exception as e:
        raise ValueError(f'An error occurred: {str(e)}')
