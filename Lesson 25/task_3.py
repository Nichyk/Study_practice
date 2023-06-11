# Implement a queue using a singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyNodeQueue:
    def __init__(self):
        self.queue = list()
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def put(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.queue.append(new_node)

    def get(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        last = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.queue.pop()
        return last


if __name__ == '__main__':
    q = MyNodeQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.queue)
    print(q.get())
    print(q.queue)
