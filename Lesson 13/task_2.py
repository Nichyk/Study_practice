# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def shout_something_to_serge(text, name):
    def shout():
        return text.upper() + ' ' + name

    def not_shout():
        return text + ' ' + name
    if name == 'Serge':
        return shout
    else:
        return not_shout


print(shout_something_to_serge('Hello', 'Serge')())


def add_five_twice(x):
    result = x + 5 + 5
    return result


def delete_five(func):
    def result_func(x):
        result = func(x) - 5
        return result
    return result_func


result_of_func = delete_five(add_five_twice)
print(result_of_func(6))
