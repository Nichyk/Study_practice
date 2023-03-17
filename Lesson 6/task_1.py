import random
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
list_of_random_numbers = list()
while len(list_of_random_numbers) < 10:
    list_of_random_numbers.append(random.randint(1, 10))
    if len(list_of_random_numbers) == 10:
        # print(list_of_random_numbers) виконується для наглядності.
        print(max(list_of_random_numbers), list_of_random_numbers)
