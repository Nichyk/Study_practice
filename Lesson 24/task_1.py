# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.
from typing import Any


class MyStack:
    def __init__(self) -> None:
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self) -> Any:
        if len(self.stack) == 0:
            return None
        last = self.stack.pop()
        return last

    def is_empty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def reverse_print(self):
        while not self.is_empty():
            print(self.stack.pop())
