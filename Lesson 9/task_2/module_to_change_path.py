import sys
print(sys.path)

try:
    import summary_of_two
except ModuleNotFoundError:
    print('You must add path to module before you import it')

sys.path.insert(0, 'C:\\Users\\nichy\\Study\\BeetrootAcademy\\Study_practice\\Lesson 9\\task_2\\another_path')

try:
    import summary_of_two
except ModuleNotFoundError:
    print('You must add path to module before you import it')

help(summary_of_two)
sum_of_two(3, 4)
