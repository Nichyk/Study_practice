from typing import List


class Solution:
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while count < len(sandwiches):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students.pop(0))
                count += 1
        return len(students)
