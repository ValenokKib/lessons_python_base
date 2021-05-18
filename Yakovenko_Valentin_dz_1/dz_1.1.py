duraction = int(input('Введите время в секундах: '))

h = duraction // 3600
min = (duraction - h * 3600) // 60
sec = duraction - (h * 3600 + min * 60)

print('Ваше время: ',  h, ' часов', min, ' минут', sec, 'секунд')