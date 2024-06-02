"""
This module provides basic arithmetic operations.
"""

def add(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first integer.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of the subtraction.
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of the two integers.
    """
    return a * b

def divide(a: int, b: int) -> float:
    """
    Divides the first integer by the second integer.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        float: The quotient of the division.

    Raises:
        ValueError: If the second integer (divisor) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
