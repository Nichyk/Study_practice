# Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces,
# and curly brackets are "balanced."

def balanced(sequence: str) -> bool:
    if sequence.count('{') != sequence.count('}') or sequence.find('{') > sequence.find('}'):
        print('\'{}\' not balanced')
        return False
    elif sequence.count('[') != sequence.count(']') or sequence.find('[') > sequence.find(']'):
        print('\'[]\' not balanced')
        return False
    elif sequence.count('(') != sequence.count(')') or sequence.find('(') > sequence.find(')'):
        print('\'()\' not balanced')
        return False
    else:
        return True
