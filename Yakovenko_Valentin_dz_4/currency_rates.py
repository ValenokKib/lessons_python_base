from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

def currency_rates(code):
    for i in content.split('<Valute ID'):
        if code.upper() in i:
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('eur'))
else:
    code = input('Введите код валюты: ')
    print(currency_rates(code))