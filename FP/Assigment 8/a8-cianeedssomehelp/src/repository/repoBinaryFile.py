from src.domain.book import Book
from src.repository.repoMemory import BookRepo
from src.repository.repoMemory import ClientRepo
from src.repository.repoMemory import RentalRepo
import pickle

class BookBinaryFileRepository(BookRepo):
    def __init__(self):
        super().__init__()
        self._filename = "books.pickle"
        self._data = self.get_all_books()

    def add_book(self, entity):
        super().add(entity)
        books = self.get_all_books()
        self._write_all(books)

    def remove_book(self, entity):
        books = self.get_all_books()
        books = [b for b in books if b != entity]
        self._write_all(books)

    def get_all_books(self):
        if not self._data:
            try:
                with open(self._filename, 'rb') as file:
                    self._data = pickle.load(file)
            except (FileNotFoundError, EOFError):
                self._data = []
        return self._data

    def clear(self):
        self._write_all([])

    def _write_all(self, books):
        print(f"Saving {len(books)} books to {self._filename}")  # Debug log
        with open(self._filename, "wb") as file:
            pickle.dump(books, file)


class ClientBinaryFileRepository(ClientRepo):
    def __init__(self):
        super().__init__()
        self._filename = "clients.pickle"
        self._data = self.get_all_clients()

    def add_client(self, entity):
        super().add(entity)
        clients = self.get_all_clients()
        self._write_all(clients)

    def remove_client(self, entity):
        clients = self.get_all_clients()
        clients = [c for c in clients if c != entity]
        self._write_all(clients)

    def get_all_clients(self):
        if not self._data:
            try:
                with open(self._filename, 'rb') as file:
                    self._data = pickle.load(file)
            except (FileNotFoundError, EOFError):
                self._data = []
        return self._data

    def clear(self):
        self._write_all([])

    def _write_all(self, clients):
        with open(self._filename, 'wb') as file:
            pickle.dump(clients, file)


class RentalsBinaryFileRepository(RentalRepo):
    def __init__(self):
        super().__init__()
        self._filename = "rentals.pickle"
        self._data = self.get_all_rentals()

    def add_rental(self, entity):
        super().add(entity)
        rentals = self.get_all_rentals()
        self._write_all(rentals)

    def remove_rental(self, entity):
        rentals = self.get_all_rentals()
        rentals = [r for r in rentals if r != entity]
        self._write_all(rentals)

    def get_all_rentals(self):
        if not self._data:
            try:
                with open(self._filename, 'rb') as file:
                    self._data = pickle.load(file)
            except (FileNotFoundError, EOFError):
                self._data = []
        return self._data

    def clear(self):
        self._write_all([])

    def _write_all(self, rentals):
        with open(self._filename, 'wb') as file:
            pickle.dump(rentals, file)