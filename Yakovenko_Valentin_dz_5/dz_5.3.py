tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

list_klass = ((tutors[i],  klasses[i] if len(klasses) > i else (tutors[i], None) for i in range(len(tutors))))

print(type(list_klass), *list_klass)
print(next(list_klass))
