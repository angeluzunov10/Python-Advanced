from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ("com", "net", "bg", "org")
MIN_NAME_SYMBOLS_COUNT = 4

pattern_for_name = r'\w+'

email = input()

while email != "End":
    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email must contain only one @ symbol!")

    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    elif len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters")

    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")

    elif findall(pattern_for_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, numbers amd underscores")

    print("Email is valid")

    email = input()
