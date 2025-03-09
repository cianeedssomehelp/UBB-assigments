from random import randint
from src.domain.rental import Rental
from src.domain.client import Client
from src.domain.book import Book
from src.domain.rentalValidator import RentalValidator
from datetime import date, timedelta
from src.repository.repoMemory import RentalRepo
from src.services.book_service import BookServices
from src.services.client_service import ClientServices
from src.services.undo_service import UndoService, FunctionCall, Operation, CascadedOperation

class BookRentalException(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Repository Exception: " + self.__msg

class BookRentalCountDTO:
    def __init__(self, book, number_of_rents):
        self._book = book
        self._number_of_rents = number_of_rents

    @property
    def book(self):
        return self._book

    @property
    def number_of_rents(self):
        return self._number_of_rents

    def __str__(self):
        return "The number of rentals: " + str(self.number_of_rents) + " for book [ " + str(self.book) + " ]"

class ClientRentalCountDTO:
    def __init__(self, client, number_of_rents):
        self._client = client
        self._number_of_rents = number_of_rents

    @property
    def client(self):
        return self._client

    @property
    def number_of_rents(self):
        return self._number_of_rents

    def __le__(self, other):
        pass

    def __str__(self):
        return "Number of days: " + str(self.number_of_rents) + " the client [ " + str(self.client) + " ] has rented books."

class AuthorRentalCountDTO:
    def __init__(self, author, number_of_rents):
        self._author = author
        self._number_of_rents = number_of_rents

    @property
    def author(self):
        return self._author

    @property
    def number_of_rents(self):
        return self._number_of_rents

    def __le__(self, other):
        pass

    def __str__(self):
        return "Number of rentals: " + str(self.number_of_rents) + " - Author " + str(self.author) + " has."


class RentalService:
    def __init__(self, repo: RentalRepo, clientService: ClientServices, bookService: BookServices, rentalValidator: RentalValidator, undo_service):
        self.repo = repo
        self.__clientService = clientService
        self.__bookService = bookService
        self.__rentalValidator = rentalValidator
        self._undo_service = undo_service

    def get(self, rental_id: int) -> Rental:
        return self.repo[rental_id]

    def add(self, rental_id: int, end: date, start: date, client: Client, book: Book):

        rental = Rental(rental_id, end, start, book, client)
        self.__rentalValidator.validate(rental)

        if self.is_book_available(rental.book, rental.rented_date, rental.returned_date) is False:
            raise BookRentalException("The book " + rental.book + " is not available.")

        self.repo.add(rental)

        functionRedo = FunctionCall(self.repo.add, rental)
        functionUndo = FunctionCall(self.repo.remove, rental_id)
        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))
        return rental

    def remove(self, rental_id: int):
        rental = self.repo.remove(rental_id)

        functionRedo = FunctionCall(self.repo.remove, rental_id)
        functionUndo = FunctionCall(self.repo.add, rental)
        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))

        return rental

    def statistics_by_most_rented_books(self):
        rental_count_dict = {}

        for rental in self.repo:
            if rental.book.id not in rental_count_dict:
                rental_count_dict[rental.book.id] = 1
            else:
                rental_count_dict[rental.book.id] += 1

        result = []
        for key in rental_count_dict:
            book = self.__bookService.get(key)
            result.append(BookRentalCountDTO(book, rental_count_dict[key]))

        result.sort(key=lambda x: x.number_of_rents, reverse=True)
        return result

    def is_book_available(self, book, start, end):
        rentals = self.filter_rentals(None, book)
        for rental in rentals:
            if start > rental.returned_date or end < rental.rented_date:
                continue
            return False
        return True

    def statistics_by_most_active_clients(self):
        clients_count_dict = {}
        for rental in self.repo:
            rental_days = len(rental)

            if rental.client.id not in clients_count_dict:
                clients_count_dict[rental.client.id] = rental_days
            else:
                clients_count_dict[rental.client.id] += rental_days
        result = []
        for key in clients_count_dict:
            client = self.__clientService.get(key)
            result.append(ClientRentalCountDTO(client, clients_count_dict[key]))
        result.sort(key=lambda x: x.number_of_rents, reverse=True)
        return result

    def statistics_by_most_rented_author(self):
        authors_count_dict = {}
        for rental in self.repo:
            book = rental.book
            author = book.author
            if author not in authors_count_dict:
                authors_count_dict[author] = 1
            else:
                authors_count_dict[author] += 1
        result = []
        for key in authors_count_dict:
            author = self.__bookService.get_author(key)
            result.append(AuthorRentalCountDTO(author, authors_count_dict[key]))
        result.sort(key=lambda x: x.number_of_rents, reverse=True)
        return result

    def filter_rentals(self, client, book):
        result = []
        for rental in self.repo.get_all_rentals():
            if client is not None and rental.client != client:
                continue
            if book is not None and rental.book != book:
                continue
            result.append(rental)
        return result

    def generate_rentals(self, book_list: [Book], client_list: [Client]):
        if not book_list or not client_list:
            print("Cannot generate rentals: Books or clients are missing.")
            return []

        rental_list = []
        for rental_id in range(50, 70):
            try:
                start_date = date(2025, randint(1, 12), randint(1, 28))
                rental_days = timedelta(days=randint(5, 10))
                book = book_list[randint(0, len(book_list) - 1)]
                client = client_list[randint(0, len(client_list) - 1)]
                rental = Rental(rental_id, start_date + rental_days, start_date, book, client)
                self.repo.add(rental)
                rental_list.append(rental)
            except Exception as e:
                raise Exception(e)
        return rental_list
