from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, repeat=False):
    '''
    функция get_jokes(), возвращает n шуток,
    сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
    :return: список шуток
    '''

    result = []
    while n:
        if repeat:
            joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
            result.append(joke)
        else:
            joke = f"{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))}" \
                   f" {adjectives.pop(randrange(len(adjectives)))}"
            result.append(joke)
        n -= 1
    return result

num_jokes = int(input('Введите число: '))

print(get_jokes(num_jokes, True))