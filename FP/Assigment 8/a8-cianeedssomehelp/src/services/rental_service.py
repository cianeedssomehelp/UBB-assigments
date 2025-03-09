from random import randint
from src.domain.rental import Rental
from src.domain.client import Client
from src.domain.book import Book
from src.domain.rentalValidator import RentalValidator
from datetime import date, timedelta
from src.repository.repoMemory import RentalRepo
from src.services.book_service import BookServices
from src.services.client_service import ClientServices

class RentalService:
    def __init__(self, repo: RentalRepo, clientService: ClientServices, bookService: BookServices, rentalValidator: RentalValidator):
        self.repo = repo
        self.__clientService = clientService
        self.__bookService = bookService
        self.__rentalValidator = rentalValidator

    def get(self, rental_id: int) -> Rental:
        return self.repo[rental_id]

    def add(self, rental_id: int, end: date, start: date, client: Client, book: Book):
        if not isinstance(book, Book):
            raise TypeError("This is not a book!")
        if not isinstance(client, Client):
            raise TypeError("This is not a client!")
        newrental = Rental(rental_id, start, end, book, client)
        self.__rentalValidator.validate(newrental)
        self.repo.add(newrental)

    def remove(self, rental_id: int):
        for existing_rental in self.repo.get_all_rentals():
            if existing_rental.id == rental_id:
                self.repo.remove(existing_rental)

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
                rental_days = timedelta(days=randint(1, 10))
                book = book_list[randint(0, len(book_list) - 1)]
                client = client_list[randint(0, len(client_list) - 1)]
                rental = Rental(rental_id, start_date + rental_days, start_date, book, client)
                self.repo.add(rental)
            except Exception as e:
                raise Exception(e)
        return rental_list
