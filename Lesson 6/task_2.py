import random
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
list_of_random_numbers_1 = list()
list_of_random_numbers_2 = list()
while len(list_of_random_numbers_1) < 10:  # Для перевірки достатньо довжини одного списку.
    list_of_random_numbers_1.append(random.randint(1, 10))
    list_of_random_numbers_2.append(random.randint(1, 10))
    if len(list_of_random_numbers_1) == 10:  # Для перевірки достатньо довжини одного списку.
        # print(list_of_random_numbers 1 та 2 виконується для наглядності.
        print(list(set(list_of_random_numbers_1 + list_of_random_numbers_2)), list_of_random_numbers_1,
              list_of_random_numbers_2)
