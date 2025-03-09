from src.repository.repoMemory import RentalRepo
from src.domain.rental import Rental
from datetime import datetime
from src.repository.repoMemory import BookRepo
from src.domain.book import Book
from src.repository.repoMemory import ClientRepo
from src.domain.client import Client
from copy import deepcopy

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

class BookTextFileRepo(BookRepo):
    def __init__(self):
        self._filename = "books.txt"
        self._history = []
        self._data = []
        if self.__loadfile():
            return
        else:
            super().__init__()

    def __loadfile(self):
        """
        Loads the books from a text file.
        """
        try:
            with open(self._filename, "rt") as fin:
                lines = fin.readlines()
        except IOError:
            print(f"Error: Could not open file '{self._filename}'.")
            return False
        for line in lines:
            if line.strip() == "":
                continue
            line = line.strip()
            parts = line.split(", ")
            book_id = int(parts[0].split("Id: ")[1])
            title = parts[1].split("Title: ")[1]
            author = parts[2].split("Author: ")[1]
            book = Book(book_id, title, author)
            self._data.append(book)
        fin.close()
        if len(self._data) == 0:
            return False
        return True

    def __saveFile(self):
        try:
            with open(self._filename, "wt") as fout:
                for book in super().get_all_books():
                    book_string = f"{book.id}, Title: {book.title}, Author: {book.author}\n"
                    fout.write(book_string)
            fout.close()
        except IOError as e:
            raise RepositoryError(f"Error saving file: {str(e)}")

    def add_book(self, book):
        super().add(book)
        self.__saveFile()


class ClientTextFileRepo(ClientRepo):
    def __init__(self):
        self._filename = "clients.txt"
        self._history = []
        self._data = []
        if self.__loadfile():
            self._history.append(deepcopy(self._data))
        else:
            super().__init__()

    def __loadfile(self):
        """
        Loads the clients into a text file.
        """
        try:
            with open(self._filename, "rt") as fin:
                lines = fin.readlines()
        except IOError:
            return False

        for line in lines:
            if line.strip() =="":
                continue

            line = line.strip()
            parts = line.split(", ")
            client_id = int(parts[0].split("Id: ")[1])
            name = parts[1].split("Name: ")[1]

            client = Client(client_id, name)
            self._data.append(client)
        fin.close()
        if len(super().get_all_clients()) == 0:
            return False
        return True

    def __saveFile(self):
        """
        Saves the clients into a text file.
        """
        try:
            with open(self._filename, "wt") as fout:
                for client in super().get_all_clients():
                    client_string = f"Id: {client.id}, Name: {client.name}\n"
                    fout.write(client_string)
            fout.close()
        except IOError:
            raise RepositoryError("Save file not found.")

    def add_client(self, client):
        super().add(client)
        self.__saveFile()

class RentalTextFileRepo(RentalRepo):
    def __init__(self, book_repo: BookRepo, client_repo: ClientRepo):
        self._filename = "rentals.txt"
        self.book_repo = book_repo
        self.client_repo = client_repo
        self._data = []
        self._history = []
        if self.__loadfile():
            self._history.append(deepcopy(self._data))
        else:
            super().__init__()

    def __loadfile(self):
        """
        Loads the rentals into a text file.
        """
        try:
            fin = open(self._filename, "rt")
            lines = fin.readlines()
        except IOError:
            return False
        for line in lines:
            tokens = line.split(",")
            rental_id = int(tokens[0])
            book_id = int(tokens[3].split("Id: ")[1])
            client_id = int(tokens[6].split("Id: ")[1])
            start = tokens[1]
            end = tokens[2].strip()
            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")
            book = self.book_repo.find_by_id(book_id)
            client = self.client_repo.find_by_id(client_id)
            rental = Rental(rental_id, end_date, start_date, book, client)
            self._data.append(rental)
        fin.close()
        if len(super().get_all_rentals()) == 0:
            return False
        return True

    def __saveFile(self):
        """
        Saves the rentals into a text file.
        """
        try:
            with open(self._filename, "wt") as fout:
                for rental in super().get_all_rentals():
                    rental_string = (
                        f"{rental.id},{rental.rented_date},{rental.returned_date}, "
                        f"Id: {rental.book.id}, Title: {rental.book.title}, Author: {rental.book.author}, "
                        f"Client Id: {rental.client.id}, Name: {rental.client.name}\n"
                    )
                    fout.write(rental_string)
            fout.close()
        except IOError:
            raise RepositoryError("Save file not found.")

    def add(self, rental: Rental):
        super().add(rental)
        self.__saveFile()