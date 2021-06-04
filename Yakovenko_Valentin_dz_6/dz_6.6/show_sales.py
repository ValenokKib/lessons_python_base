from sys import argv

def main(argv):
    if len(argv) == 1:
        with open('bakery.csv', 'r', encoding='utf-8') as val:
            content = val.read()
            print(f'{content}')
    elif len(argv) == 2:
        with open('bakery.csv', 'r', encoding='utf-8') as val:
            content = val.readlines()
            print(''.join(content[int(argv[1]):]))
    elif len(argv) == 3:
        with open('bakery.csv', 'r', encoding='utf-8') as val:
            content = val.readlines()
            print(''.join(content[int(argv[1]):int(argv[2])]))


if __name__ == '__main__':
    main(argv[0:])
