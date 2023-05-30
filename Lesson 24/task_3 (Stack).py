# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message
from task_1 import MyStack


class ExtendedMyStack(MyStack):
    def __init__(self) -> None:
        self.sequence = list()
        super().__init__()

    def get_from_stack(self, item):
        if item not in self.sequence:
            raise ValueError(f'{item} not in stack')
        else:
            return self.sequence.pop(self.sequence.index(item))
