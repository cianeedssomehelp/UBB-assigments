

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
        if self.find_by_id(book.id) is not None:
            raise ValueError("Cannot add a none object to the repository.")
        self._data.append(book)

    def remove(self, book_id):
        book = self.find_by_id(book_id)
        if book is None:
            raise RepositoryError("Cannot remove a none object from the repository.")
        self._data.remove(book)
        return book

    def update(self, book):
        element = self.find_by_id(book.id)
        if element is None:
            raise RepositoryError("Cannot update a none object from the repository.")
        index = self._data.index(element)
        self._data.remove(element)
        self._data.insert(index, book)

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
        for book in self._data:
            if book.id == book_id:
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
        if self.find_by_id(client.id) is not None:
            raise ValueError("Cannot add a none object to the repository.")
        self._data.append(client)

    def remove(self, client_id):
        client = self.find_by_id(client_id)
        if client is None:
            raise RepositoryError("Cannot remove a none object from the repository.")
        self._data.remove(client)
        return client

    def update(self, client):
        element = self.find_by_id(client.id)
        if element is None:
            raise RepositoryError("Cannot update a none object from the repository.")
        index = self._data.index(element)
        self._data.remove(element)
        self._data.insert(index, client)

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
        for client in self._data:
            if client.id == client_id:
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
        if self.get_rental(rental.id) is not None:
            raise RepositoryError(f"Cannot add a none object from the repository.")
        self._data.append(rental)

    def remove(self, rental_id):
        rental = self.get_rental(rental_id)

        if rental is None:
            raise RepositoryError(f"Cannot remove a none object from the repository.")

        try:
            self._data.remove(rental)
        except ValueError as e:
            raise RepositoryError(f"Error while removing rental with ID {rental_id}: {e}")

        return rental

    def get_all_rentals(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def clear(self):
        self._data.clear()

    def __iter__(self):
        return RepositoryIterator(list(self._data))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]