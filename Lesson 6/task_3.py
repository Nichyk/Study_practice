# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration.
list_of_integers = list()
appropriate_values = list()
number = 0
while len(list_of_integers) < 100:
    number += 1
    list_of_integers.append(number)
    if number % 7 == 0 and number % 5 != 0:
        appropriate_values.append(number)
print(appropriate_values, list_of_integers)  # print(list_of_integers) для наглядності.
