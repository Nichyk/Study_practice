# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words(words: list):
    def inside_func(func):
        def wrapper(*args, **kwargs):
            message = func(*args, **kwargs)
            for i in words:
                message = message.replace(i, '*')
            return message
        return wrapper
    return inside_func


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
