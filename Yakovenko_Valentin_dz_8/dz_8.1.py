import re

def email_parse(email_address):
    RE_email = re.compile(r'(?P<name>[a-z0-9_.-]+)@(?P<host>[a-z0-9]+\.\w+)', re.IGNORECASE)
    if not RE_email.match(email_address):
        raise ValueError(f'некорректный @mail: {email_address}')
    print(RE_email.search(email_address).groupdict())

email = 'SJJncnuuukrya@kryakrya.ua'
print(email_parse(email))
