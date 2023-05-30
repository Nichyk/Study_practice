class Person:
    def __init__(self, name, gender, age, occupation) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation

    def talk(self) -> str:
        return f'Hi, I am {self.name} and I am a {self.occupation}'

    def birth(self):
        return f'{self.name} birth in ' + str(2023 - self.age)


class Student(Person):
    def __init__(self, name, gender, age, classroom, scholarship, occupation='student') -> None:
        super().__init__(name, gender, age, occupation)
        self.classroom = classroom
        self.scholarship = scholarship


class Teacher(Person):
    def __init__(self, name, gender, age, salary, occupation='teacher') -> None:
        super().__init__(name, gender, age, occupation)
        self.salary = salary


student1 = Student('Joe', 'male', 21, 'A', 2000)
print(student1.talk(),  student1.birth(), student1.scholarship, sep='\n')
teacher1 = Teacher('George', 'male', 45, 5000)
print(teacher1.talk(), teacher1.birth(), teacher1.salary, sep='\n')
