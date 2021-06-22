from abc import ABC, abstractmethod

class Clothes:
    """ clothes """
    def __init__(self, v = 0, h = 0):
        self.v = v
        self.h = h
    @property
    @abstractmethod
    def consumption(self):
        pass

    def coat(self):
        return f"Расход ткани для пальто: {self.v / 6.5 + 0.50}"

    @property
    def suit(self):
        return f"Расход ткани для косттюма: {2 * self.h + 0.3}"

    def __add__(self, other):
        return Clothes(self.v + other.v, self.h + other.h)

    def __str__(self):
        return f"Параметры: {self.v}, {self.h}"

a = Clothes(100, 5)
a2 = Clothes(20, 66)
print(a.coat())
print(a.suit)
print(f"{a + a2}")