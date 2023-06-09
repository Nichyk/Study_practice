# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
# з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції
# порівняння між об'єктами класу Fraction
from math import lcm
from dataclasses import dataclass


@dataclass
class Fraction:
    nom: float
    denom: float

    def __add__(self, other):
        new_denom = lcm(int(self.denom), other.denom)
        left_nom = new_denom * self.nom / self.denom
        right_nom = new_denom * other.nom / other.denom
        return Fraction(nom=left_nom + right_nom, denom=new_denom)

    def __sub__(self, other):
        new_denom = lcm(int(self.denom), other.denom)
        left_nom = new_denom * self.nom / self.denom
        right_nom = new_denom * other.nom / other.denom
        return Fraction(nom=left_nom - right_nom, denom=new_denom)

    def __mul__(self, other):
        return Fraction(nom=self.nom * other.nom, denom=self.denom * other.denom)

    def __truediv__(self, other):
        new_other_nom, new_other_denom = other.denom, other.nom
        return Fraction(nom=self.nom * new_other_nom, denom=self.denom * new_other_denom)

    def __lt__(self, other):
        return self.nom / self.denom < other.nom / other.denom

    def __eq__(self, other):
        return self.nom / self.denom == other.nom / other.denom

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    assert x + y == Fraction(3, 4)
