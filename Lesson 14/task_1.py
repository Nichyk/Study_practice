# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
def my_logger(func):
    def wrapper(*args):
        result = func(*args)
        print(f'{func.__name__} called with {", ".join([str(item) for item in args])}')
        return result
    return wrapper


@my_logger
def add(x, y):
    return x + y

@my_logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(7, 2))
print(square_all(7, 1, 2))
