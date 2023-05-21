# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message
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

    def get_from_stack(self, item):
        if item not in self.sequence:
            raise ValueError(f'{item} not in stack')
        else:
            index = self.sequence.index(item)
            return self.sequence.pop(index)
