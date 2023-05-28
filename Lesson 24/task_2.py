# Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces,
# and curly brackets are "balanced."
from collections import deque


def balanced(sequence: str) -> bool:
    stack = deque()
    brackets = {')': '(', '}': '{', ']': '['}
    if len(sequence) <= 1:
        return False
    for i in sequence:
        if i in brackets.values():
            stack.append(i)
        if i in brackets.keys():
            if len(stack) == 0:
                return False
            else:
                stack.append(i)
                if stack.count(i) != stack.count(brackets[i]):
                    return False
    return True


if __name__ == '__main__':
    print(balanced('()'))
    print(balanced('()[]{}'))
    print(balanced('(]'))










