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
        if len(self.sequence) == 0:
            return True
        else:
            return False

    def reverse_print(self):
        while not self.is_empty():
            print(self.sequence.pop())
