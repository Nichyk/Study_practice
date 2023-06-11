# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message
from typing import Any
from task_1 import MyStack


class ExtendedMyStack(MyStack):
    def get_from_stack(self, item) -> Any:
        if item in self.stack:
            temp = list()
            for i in range(len(self.stack)):
                last = self.stack.pop()
                if last != item:
                    temp.append(last)
                else:
                    self.stack += temp[::-1]
                    return last
        else:
            raise ValueError('Element was not found')


if __name__ == '__main__':
    d = ExtendedMyStack()
    d.push(55)
    d.push(2)
    d.push(3)
    d.push(4)
    print(d.stack)
    print(d.get_from_stack(2))
    print(d.stack)
