# Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# `start`, `end`, and optional step. Tips: See the documentation for `range` function
def in_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step
