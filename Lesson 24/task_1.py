# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

class MyStack:
    def __init__(self):
        self.sequence = list()

    def push(self, item):
        self.sequence.append(item)

    def pop(self):
        return self.sequence.pop()

    def is_empty(self):
        if len(self.sequence) == 0:
            return True
        else:
            return False

    def reverse_print(self):
        if self.is_empty():
            return 'Sequence is empty'
        else:
            return self.sequence[::-1]
