# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
from typing import List


class Mathematician:
    @staticmethod
    def square_nums(nums: List[int]) -> List[int]:
        result = list(map(lambda x: x**2, nums))
        return result

    @staticmethod
    def remove_positives(nums: List[int]) -> List[int]:
        result = list(filter(lambda x: x <= 0, nums))
        return result

    @staticmethod
    def filter_leaps(nums: List[int]) -> List[int]:
        result = list(filter(lambda x: x % 4 == 0 and x % 100 != 0 or x % 400 == 0, nums))
        return result


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
