translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
            'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
             'nine': 'девять', 'ten': 'десять'}

def num_translate(num):
        return translate.get(num)

print(num_translate(input('Enter the number "from zero to ten" to translate: ')))