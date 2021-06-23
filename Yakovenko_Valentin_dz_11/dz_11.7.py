class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел: z1 + z2 = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Умножение комлпексных чисел: z1 * z2 = ' \
               f'{self.a * other.a - (self.b * other.b)} + {self.a * other.b + other.a * self.b} * i'

    def __str__(self):
        return f'= {self.a} + {self.b} * i'


z1 = ComplexNumber(3, 1)
z2 = ComplexNumber(2, -3)
print('z1', z1)
print('z2', z2)
print(z1 + z2)
print(z1 * z2)