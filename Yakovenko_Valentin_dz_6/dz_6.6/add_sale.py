from sys import argv

def add_sale(value):
    with open('bakery.csv', 'a', encoding='utf-8') as sales:
        sales.write(f'{value}\n')


if __name__ == '__main__':
    add_sale(argv[1])