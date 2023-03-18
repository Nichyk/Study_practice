# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
# Без змінної j
list_of_squares = [(i, i ** 2) for i in range(1, 11)]
print(list_of_squares)
# Якщо треба, щоб була змінна j
list_of_squares = [(i, j ** 2) for i, j in enumerate(range(1, 11), 1)]
print(list_of_squares)