procent = int(input('Введите число: '))

for procent in range(procent):
    if procent % 10 == 1 and procent % 100 != 11:
        print(procent, 'процент')
    elif (procent % 10 > 1 and procent % 10 < 5) and not (procent % 100 > 11 and procent % 100 < 15):
        print(procent, 'процента')
    else:
        print(procent, 'процентов')
