# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words(words: list):
    def inside_func(func):
        def wrapper(*args, **kwargs):
            list_to_check = func(*args, **kwargs).split(' ')
            for word in words:
                for i, v in enumerate(list_to_check):
                    if word.lower() in v.lower():
                        list_to_check[i] = '*'
            correct_message = ' '.join(list_to_check) + '!'
            return correct_message
        return wrapper
    return inside_func


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
