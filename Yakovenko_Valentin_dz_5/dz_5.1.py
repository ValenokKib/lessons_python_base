def odd(num):
    for num in range(1, num + 1, 2):
        yield num

n = int(input('Введите число: '))

for i in odd(n):
    print(i)

