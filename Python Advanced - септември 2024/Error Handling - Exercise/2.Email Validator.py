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


valid_domains = ("com", "bg", "org", "net")
min_name_symbols_count = 4

pattern_name = r"\w+"

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")

    if len(email.split("@")[0]) <= min_name_symbols_count:
        raise NameTooShortError("Name must be more than 4 characters!")

    if email.split(".")[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    print("Email is valid")
