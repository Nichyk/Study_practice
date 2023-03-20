import random
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings
# from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string
# 1
word = input('Please enter some string: ')
random_word = ''
random_index = ''
count = 0
while count < 5:
    index = random.randint(0, len(word) - 1)
    if len(random_word) < len(word):
        if str(index) not in random_index:
            random_index += str(index)
            random_word += word[index]
    else:
        print(random_word)
        random_word = ''
        random_index = ''
        count += 1
# 2
word = input('Please enter some string: ')
new_word = ''
for i in range(0, len(word)):
    new_word = ''.join(random.sample(word, k=len(word)))
    print(new_word)
