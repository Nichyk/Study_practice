# Task 1
# The greeting program.
# Make a program that has your name and the current day of the week stored as separate variables and
# then prints a message like this:
#      "Good day <name>! <day> is a perfect day to learn some python."
# Note that  <name> and <day> are predefined variables in source code.
# An additional bonus will be to use different string formatting methods for constructing result string.
my_name = 'Serhii'
current_day = 'Friday'
print(f'Good day {my_name}! {current_day} is a perfect day to learn some python.')
print('Good day {}! {} is a perfect day to learn some python.'.format(my_name, current_day))
print('Good day {my_name}! {current_day} is a perfect day to learn some python.'.format(my_name='Serhii Nichyk',
                                                                                        current_day='Every day'))
