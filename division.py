def divide_two_numbers(a, b):
    """Returns the result of division of two numbers."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
