class InvalidInputError(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Invalid Input Exception: " + self.__msg

class BookValidator:
    def validate_book(self, book):
        errors = ""
        id = book.id
        title = book.title
        author = book.author
        if not isinstance(id, int):
            errors += "Book id must be an integer"
        if not isinstance(title, str):
            errors += "Book title must be a string"
        if not isinstance(author, str):
            errors += "Book author must be a string"
        if len(errors) != 0:
            raise InvalidInputError

class ClientsValidator:
    def validate_clients(self, clients):
        errors = []
        id = clients.id
        name = clients.name
        if not isinstance(id, int):
            errors += "Client id must be an integer"
        if not isinstance(name, str):
            errors += "Client name must be a string"
        if len(errors) != 0:
            raise InvalidInputError