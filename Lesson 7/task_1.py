# Make a program that has some sentence (a string) on input and returns
# a dict containing all unique words as keys and the number of occurrences as values.
some_string = input('Enter some string: ')
# Додатково додана перевірка на випадок розділових знаків та великих літер.
new_string = ''.join([letter.lower() for letter in some_string if letter.isalpha() or letter == ' '])
new_dict = {}
for value in new_string.split(' '):
    if value not in new_dict:
        new_dict[value] = 1
    else:
        new_dict[value] += 1
print(new_dict)
