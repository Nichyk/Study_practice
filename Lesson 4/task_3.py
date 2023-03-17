# The math quiz program.
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
# and then responds with a message accordingly.
question = input('What is "4 + 4": ')
answer = 8
if question.isdigit() and int(question) == answer:
    print('You are smart!')
elif not question.isdigit():
    print('Wrong format! Please enter a number next time.')
else:
    print('Wrong answer\U0001F641')