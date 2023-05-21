# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.
from typing import List, Any


class MyStack:
    def __init__(self, sequence: List) -> None:
        self.sequence = sequence

    def push(self, item):
        self.sequence.append(item)

    def pop(self) -> Any:
        try:
            return self.sequence.pop()
        except IndexError:
            print('List is empty. Push some items and try again')

    def reverse_print(self) -> List:
        return self.sequence[::-1]
