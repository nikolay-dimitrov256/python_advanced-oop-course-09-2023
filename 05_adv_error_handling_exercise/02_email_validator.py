import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ('.com', '.bg', '.net', '.org')

while True:
    current_email = input()
    if current_email == 'End':
        break

    pattern = r'([a-zA-Z\d\-]*)(@*)[a-zA-Z\d]*(\.[a-zA-Z\d\.]*)'
    match = re.fullmatch(pattern, current_email)

    if match:
        name = match.group(1)
        at_symbol = match.group(2)
        domain = match.group(3)

        if len(name) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')

        if not at_symbol:
            raise MustContainAtSymbolError('Email must contain @')

        if domain not in valid_domains:
            raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    else:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
