from typing import List


class Solution:
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while count < len(sandwiches):
            if students[0] == sandwiches[-1]:
                students.pop(0)
                sandwiches.pop()
                count = 0
            else:
                student = students.pop(0)
                students.append(student)
                count += 1
        return len(students)


q = Solution()
print(q.count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))

