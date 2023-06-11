# Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message
from typing import Any
from queue import Queue


class MyQueue(Queue):
    def get_from_queue(self, item) -> Any:
        if item in self.queue:
            temp = list()
            for i in range(len(self.queue)):
                last = self.queue.pop()
                if last != item:
                    temp.append(last)
                else:
                    self.queue += temp[::-1]
                    return last
        else:
            raise ValueError('Element was not found')


if __name__ == '__main__':
    q = MyQueue()
    q.put(3)
    q.put(55)
    q.put(6)
    q.put(98)
    q.put(47)
    print(q.queue)
    print(q.get_from_queue(6))
    print(q.queue)
