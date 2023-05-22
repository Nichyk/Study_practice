# Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message
from typing import Any


class Queue:

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self) -> Any:
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self) -> int:
        return len(self.queue)

    def get_from_stack(self, item):
        if item not in self.queue:
            raise ValueError(f'{item} not in stack')
        else:
            index = self.queue.index(item)
            return self.queue.pop(index)
