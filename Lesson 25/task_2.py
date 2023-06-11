# Implement a stack using a singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyNodeStack:
    def __init__(self):
        self.stack = list()
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.stack.append(new_node)

    def pop(self):
        if self.is_empty():
            return IndexError('Stack is empty')
        last = self.head.data
        self.head = self.head.next
        self.stack.pop()
        return last


if __name__ == '__main__':
    q = MyNodeStack()
    q.push(1)
    q.push(2)
    print(q.stack)
    print(q.pop())
    print(q.pop())
    print(q.stack)
