import pickle
from datetime import date
from src.domain.book import Book
from src.domain.client import Client
from src.repository.repoMemory import RentalRepo


class Rental:
    def __init__(self, rental_id: int, returned_date, rented_date, book, client):
        if not isinstance(rental_id, int):
            raise TypeError('The id of the rental must be an integer.')
        if not isinstance(rented_date, date):
            raise TypeError('The rented date must be a correct time date.')
        if not isinstance(returned_date, date):
            raise TypeError('The returned date must be a correct time date.')
        if not isinstance(book, Book):
            raise TypeError('The book must be an instance of Book.')
        if not isinstance(client, Client):
            raise TypeError('The client must be an instance of Client.')
        self.__id = rental_id
        self.__book = book
        self.__client = client
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def id(self):
        return self.__id

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def returned_date(self):
        return self.__returned_date

    @property
    def book(self):
        return self.__book

    @property
    def client(self):
        return self.__client

    def __len__(self):
        if self.__returned_date is not None:
            return (self.__returned_date - self.__rented_date).days + 1
        today = date.today()
        return (today - self.__rented_date).days + 1

    def __eq__(self, other):
        return isinstance(other, Rental) and self.id == other.id

    def __repr__(self):
        return str(self)

    def __str__(self):
        # return
        from_date = self.__rented_date.strftime("%Y-%m-%d")
        to_date = self.__returned_date.strftime("%Y-%m-%d")
        return f"{self.__id} - [book {self.book}] - [client {self.client}] - from {from_date} to {to_date}"