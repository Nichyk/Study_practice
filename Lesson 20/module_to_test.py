def make_operation(operator, fixed, *args):
    """Simple calculator function"""
    result = fixed
    for value in args:
        if operator == '+':
            result += value
        elif operator == '-':
            result -= value
        elif operator == '*':
            result *= value
    return result
