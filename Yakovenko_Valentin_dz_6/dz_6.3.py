from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        if len(users.readline()) >= len(hobby.readline()):
            with open('kuku.json', 'w', encoding='utf-8') as my_file:
                my_list = zip_longest((' '.join(us.split(',')) for us in users), hobby)
                my_dict = {str(i[0]).strip(): (i[1].strip()) for i in my_list}

                dump(my_dict, my_file)
            print(my_dict)
        else:
            exit(1)

