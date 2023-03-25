# Write a function that takes in two numbers from the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by b, construct a try-except block which raises an exception
# if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).


def make_operation(a=input('Enter first arg: '), b=input('Enter second arg: ')):
    """Func that make first number squared and the divided by second number"""
    try:
        result = int(a) ** 2 / int(b)
        return f'Result is: {round(result, 2)}.'
    except ZeroDivisionError:
        return 'Can\'t be divided by 0'
    except ValueError:
        return 'Wrong type for number'


print(make_operation())
