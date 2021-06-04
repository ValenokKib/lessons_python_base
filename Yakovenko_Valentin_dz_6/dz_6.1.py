with open('ngixt_logs.txt', 'r', encoding='utf-8') as file:
    data = ((string.split()[0], string.split()[5][1:], string.split()[6]) for string in file)
    for i in data:
        print(i)
