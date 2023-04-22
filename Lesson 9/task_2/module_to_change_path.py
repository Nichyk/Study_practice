import sys
print(sys.path)

try:
    from summary_of_two import sum_of_two
except ModuleNotFoundError:
    print('You must add path to module before you import it')

sys.path.append('D:\Study_practice\Lesson 9\\task_2\\another_path')
print(sys.path)

try:
    from summary_of_two import sum_of_two
except ModuleNotFoundError:
    print('You must add path to module before you import it')

print(sum_of_two(3, 4))
