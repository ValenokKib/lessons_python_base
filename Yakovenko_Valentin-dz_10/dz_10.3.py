class Cell:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def __str__(self):
        return f"Результат: {self.data1}, {self.data2}"

    def __add__(self, other):
        return Cell(self.data1 + other.data1, self.data2 + other.data2)

    def __sub__(self, other):
        return Cell(self.data1 - other.data1, self.data2 - other.data2)

    def __mul__(self, other):
        return Cell(self.data1 * other.data1, self.data2 * other.data2)

    def __floordiv__(self, other):
        return Cell(self.data1 // other.data1, self.data2 // other.data2)

    def __truediv__(self, other):
        return Cell(self.data1 / other.data1, self.data2 / other.data2)

    def make_order(self, rows):
        x = ""
        row = int(self.data1)//rows
        for i in range(row):
            x += ("*" * rows)
            x += "\n"
        row2 = (int(self.data1) % rows)
        x += "*" * row2
        return x

a1 = Cell(12, 5)
a2 = Cell(4, 43)
print(a1.make_order(5))
print(f"Сумма: {a1 + a2}")
print(f"Разность: {a1 - a2}")
print(f"Произведение: {a1 * a2}")
print(f"Целочисленно деление: {a1 // a2}")
print(f"Деление: {a1 / a2}")