# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start` and `stop`, and return a copy of the list
# starting at the position and going up to but not including the stop position.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        next_node = self.head
        result = ''
        while next_node:
            result += str(next_node.data)
            next_node = next_node.next
        return result

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} is not in the list.")

    def pop(self, pos=None):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty list.")
        if pos is None:
            pos = self.size() - 1
        if pos == 0:
            popped_item = self.head.data
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            index = 0
            while current is not None and index < pos:
                prev = current
                current = current.next
                index += 1
            if current is None:
                raise IndexError("Index out of range.")
            popped_item = current.data
            prev.next = current.next
        return popped_item

    def insert(self, pos, item):
        if pos == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            prev = None
            current = self.head
            index = 0
            while current is not None and index < pos:
                prev = current
                current = current.next
                index += 1
            if current is None and index < pos:
                raise IndexError("Index out of range.")
            new_node = Node(item)
            new_node.next = current
            prev.next = new_node

    def slice(self, start, stop):
        if start >= stop:
            return UnorderedList()

        sliced_list = UnorderedList()
        current = self.head
        index = 0
        while current is not None:
            if start <= index < stop:
                sliced_list.append(current.data)
            current = current.next
            index += 1
        return sliced_list

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


if __name__ == '__main__':
    q = UnorderedList()
    q.append('1')
    q.append('2')
    q.append(3)
    print(q.pop())
    q.insert(0, '33')
    print(q.slice(0, 2))
    print(q.index('33'))
    print(q)
