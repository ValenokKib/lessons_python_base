def thesaurus(*args):
    names = {}
    for i in args:
        let = i[0]
        if let in names:
            names[let] += [i]
        else:
            names[let] = [i]
    return names

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марат", "Петруха", "Вася", "Валя", "Коля", "Костя"))