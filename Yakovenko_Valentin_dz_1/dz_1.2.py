my_list_cubes = []
my_list_2 = []
sum = 0

for i in range(1, 1000, 2):

    my_list_cubes.append(i ** 3)

print('Список кубов нечетных чисел: ', my_list_cubes)

for i, j in enumerate(my_list_cubes):
    n = 0
    while j > 0:
        n = n + j % 10
        j = j // 10
    if n % 7 == 0:
        sum = sum + my_list_cubes[i]

print('Сумма чисел, сумма цифр которых делится на 7 =', sum)

for i in my_list_cubes:
    my_list_2.append(i + 17)

print('Список кубов с добавлением  17: ', my_list_2)
sum = 0
for i, j in enumerate(my_list_2):
    n = 0
    while j > 0:
        n = n + j % 10
        j = j // 10
    if n % 7 == 0:
        sum = sum + my_list_2[i]

print('Сумма чисел нового списка, сумма цифр которых делится на 7 =', sum)