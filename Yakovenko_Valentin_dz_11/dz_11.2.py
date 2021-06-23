class MyErr(Exception):
    def __init__(self, ddd):
        self.ddd = ddd

num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))

try:
    if num_2 == 0:
        raise MyErr("Делить на ноль нельзя!!!!! Попробуйте снова")
except MyErr as err:
    print(err)
else:
    print(f"Результат деления: {num_1 / num_2}")
