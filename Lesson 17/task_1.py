# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
# and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs
# talk method on input parameter.
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        text = 'woof woof'
        return text


class Cat(Animal):
    def talk(self):
        text = 'meow'
        return text


cat1 = Cat()
dog1 = Dog()


def animal_talk(animal):
    if not isinstance(animal, Animal):
        raise ValueError('Not animal')
    if isinstance(animal, Dog) or isinstance(animal, Cat):
        return animal.talk()


print(animal_talk(dog1))
