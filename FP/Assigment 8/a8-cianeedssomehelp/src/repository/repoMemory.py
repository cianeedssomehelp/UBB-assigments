

class RepositoryError(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Repository Exception: " + self.__msg

class DuplicateIDError(RepositoryError):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "DuplicateIdError Exception: " + self.__msg

class IDNotFoundError(RepositoryError):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "IdNotFoundError Exception " + self.__msg

class RepositoryIterator:
    def __init__(self, data):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if len(self.__data) == self.__pos:
            raise StopIteration()

        return self.__data[self.__pos]

class BookRepo:
    def __init__(self):
        self._data = []

    def get_book(self, book_id):

        for book in self._data:
            if book.id == book_id:
                return book

    def add(self, book):
        for existing_book in self._data:
            if existing_book.id == book.id:
                raise DuplicateIDError(f"Object with {book.id} already exists.")
        self._data.append(book)

    def remove(self, book):
        self._data.remove(book)

    def update(self, book_id, updated_field, index):
        for existing_book in self._data:
            if existing_book.id == book_id:
                if index == "title":
                    existing_book.title = updated_field
                elif index == "author":
                    existing_book.author = updated_field
                else:
                    raise RepositoryError(f"Field {index} not found.")
        raise IDNotFoundError(f"Object with {book_id} not found.")

    def find(self, book_id: int, index: str, value):
        book = self.get_book(book_id)
        if not book:
            raise IDNotFoundError(f"Object with {book_id} does not exist.")
        else:
            if book_id == book.id:
                return self._data[book]
            elif index == "title" and value.lower() in book.title.lower():
                return self._data[book]
            elif index == "author" and value.lower() in book.author.lower():
                return self._data[book]
            else:
                raise RepositoryError(f"Field {index} not found.")

    def find_by_id(self, book_id):
        book = self.get_book(book_id)
        if not book:
            raise IDNotFoundError(f"Object with {book_id} does not exist.")
        if book_id == book.id:
            return book

    def get_all_books(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def clear(self):
        self._data.clear()

    def __iter__(self):
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

class ClientRepo:
    def __init__(self):
        self._data = []

    def get_client(self, client_id):
        for client in self._data:
            if client.id == client_id:
                return client

    def get_client_by_name(self, client_name):
        for client in self._data:
            if client.name == client_name:
                return client

    def add(self, client):
        for existing_client in self._data:
            if existing_client.id == client.id:
                raise DuplicateIDError(f"Object with {client.id} already exists.")
        self._data.append(client)

    def remove(self, client):
        self._data.remove(client)

    def update(self, client_id, updated_field, index):
        for existing_client in self._data:
            if existing_client.id == client_id:
                if index == "name":
                    existing_client.name = updated_field
                else:
                    raise RepositoryError(f"Field {index} not found.")
        raise RepositoryError(f"Object with {client_id} not found.")

    def find(self, client_id: int, index: str, value):
        client = self.get_client(client_id)
        if not client:
            raise RepositoryError(f"Object with {client_id} does not exist.")
        else:
            if client_id == client.id:
                return self._data[client]
            elif index == "name" and value.lower() in client.name.lower():
                return self._data[client]
            else:
                raise RepositoryError(f"Field {index} not found.")

    def find_by_id(self, client_id):
        client = self.get_client(client_id)
        if not client:
            raise RepositoryError(f"Object with {client_id} does not exist.")
        if client_id == client.id:
            return client

    def get_all_clients(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def clear(self):
        self._data.clear()

    def __iter__(self):
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

class RentalRepo:
    def __init__(self):
        self._data = []

    def get_rental(self, rental_id):
        for rental in self._data:
            if rental.id == rental_id:
                return rental

    def add(self, rental):
        for existing_rental in self._data:
            if existing_rental.id == rental.id:
                raise RepositoryError(f"Object with {rental.id} already exists.")
        self._data.append(rental)

    def remove(self, rental):
        self._data.remove(rental)

    def get_all_rentals(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def clear(self):
        self._data.clear()

    def __iter__(self):
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]