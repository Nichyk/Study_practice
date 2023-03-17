import random
# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
answer = random.randint(1, 10)
question = input('What number was generated?: ')
if question.isdigit() and int(question) == answer:
    print('You are right!')
else:
    print(f'You are wrong. The number was {answer}.')