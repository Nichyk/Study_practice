# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.
class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

    def __getitem__(self, index):
        return self.data[index]
