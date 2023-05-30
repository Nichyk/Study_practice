# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.
from typing import Any


class MyStack:
    def __init__(self) -> None:
        self.sequence = list()

    def push(self, item):
        self.sequence.append(item)

    def pop(self) -> Any:
        return self.sequence.pop()

    def is_empty(self) -> bool:
        return True if len(self.sequence) == 0 else False

    def index(self, index):
        for i, v in enumerate(self.sequence, 1):
            if index == i:
                return v

    def reverse_print(self):
        while not self.is_empty():
            print(self.sequence.pop())
