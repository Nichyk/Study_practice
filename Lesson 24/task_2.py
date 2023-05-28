# Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces,
# and curly brackets are "balanced."
from collections import deque


def balanced(sequence: str) -> bool:
    stack = deque()
    brackets = {')': '(', '}': '{', ']': '['}
    if len(sequence) != 0 and not len(sequence) % 2:
        for i in sequence:
            if i in brackets.values():
                stack.append(i)
            elif i in brackets.keys() and len(stack) == 0:
                return False
            elif i in brackets.keys() and stack[-1] != brackets[i]:
                return False
            else:
                stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    print(balanced('()'))
    print(balanced('()[]{}'))
    print(balanced('(]'))
    print(balanced('({{{{}}}))'))
    print(balanced("([)]"))
    print(balanced("{[]}"))
