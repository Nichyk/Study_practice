def count_lines(name):
    """Func to count strings in file"""
    file_to_count_in = open(name, 'r')
    return len(file_to_count_in.readlines())


def count_chars(name):
    """Func to count chars in file"""
    file_to_count_in = open(name, 'r')
    return len(file_to_count_in.read())


def test(name):
    """Func to call count_lines and count_chars"""
    lines = count_lines(name)
    chars = count_chars(name)
    print(f'This {name} file has {lines} lines and {chars} chars!')
