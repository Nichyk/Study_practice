# Imports practice
# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.
from random import sample
from module_with_function import greeting

list_with_numbers = [1, 2, 3, 4, 5, 6, 7]
list_with_random_numbers = sample(list_with_numbers, k=5)
for number in list_with_random_numbers:
    if number == 7:
        print('There was 7')
        continue
    greeting(number)
