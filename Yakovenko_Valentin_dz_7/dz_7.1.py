import os

my_pack = {'my_project': [{'setting': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for i, j in my_pack.items():
    if not os.path.exists(i):
        for item in j:
            for key in item.keys():
                os.makedirs(os.path.join(i, key))
