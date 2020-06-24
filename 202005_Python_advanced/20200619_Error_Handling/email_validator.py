class NameTooShortError(Exception):
    """ raise it when the name in the email is less than or equal to 4 """
    def __init__(self, message="Name must be more than 4 characters"):
        self.message = message
        super().__init__(message)


class MustContainAtSymbolError(Exception):
    """ Email must contain @ """
    def __init__(self, message="Email must contain @"):
        self.message = message
        super().__init__(message)


class InvalidDomainError(Exception):
    """ Domain must be one of the following: .com, .bg, .org, .net """
    def __init__(self, message="omain must be one of the following: .com, .bg, .org, .net"):
        self.message = message
        super().__init__(message)


def validate_name(email):
    user_name = email.split("@")[0]
    if len(user_name) <= 4:
        # raise NameTooShortError("Name must be more than 4 characters")
        raise NameTooShortError()


def validate_at_symbol(email):
    if "@" not in email:
        # raise MustContainAtSymbolError("Email must contain @")
        raise MustContainAtSymbolError()


def validate_domain(email, valid_domains):
    domain = email.split(".")[-1]
    if domain not in valid_domains:
        # raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        raise InvalidDomainError()


while True:
    line = input()
    valid_domains = ("com", "net", "bg", "org")

    if line == "End":
        break

    validate_name(line)
    validate_at_symbol(line)
    validate_domain(line, valid_domains)

    print("Email is valid")
