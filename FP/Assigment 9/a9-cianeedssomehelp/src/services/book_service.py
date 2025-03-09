from random import randint
from src.repository.repoMemory import BookRepo
from src.domain.book import Book
from src.domain.bookandclientvalidator import BookValidator
from src.services.undo_service import FunctionCall, Operation, UndoService, CascadedOperation
from copy import deepcopy


class BookServices:
    def __init__(self, repo: BookRepo, rental_repo, bookValidator: BookValidator, undo_service):
        self.repo = repo
        self.rentals_repo = rental_repo
        self.__bookValidator = bookValidator
        self._undo_service = undo_service

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.__bookValidator.validate_book(book)
        self.repo.add(book)

        functionRedo = FunctionCall(self.repo.add, book)
        functionUndo = FunctionCall(self.repo.remove, book_id)

        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))
        return book

    def remove_book(self, book_id):
        rentals_to_remove = [
            rental for rental in self.rentals_repo.get_all_rentals()
            if rental.book.id == book_id
        ]

        for rental in rentals_to_remove:
            self.rentals_repo.remove(rental.id)

        book = self.repo.remove(book_id)

        functionRedo = FunctionCall(self.repo.remove, book_id)
        functionUndo = FunctionCall(self.repo.add, book)
        operations = [Operation(functionUndo, functionRedo)]

        for rental in rentals_to_remove:
            functionRedo = FunctionCall(self.rentals_repo.remove, rental.id)
            functionUndo = FunctionCall(self.rentals_repo.add, rental)
            operations.append(Operation(functionUndo, functionRedo))

        self._undo_service.recordUndo(CascadedOperation(*operations))

    def update_book(self, book_id, title, author):
        original_book = self.repo.get_book(book_id)
        if original_book is None:
            raise ValueError("Book not found.")

        original_state = deepcopy(original_book)
        print(type(original_state))

        for book in self.repo.get_all_books():
            if book.id == book_id:
                book.set_title(title)
                book.set_author(author)
        newbook = Book(book_id, title, author)
        print(str(newbook))
        functionRedo = FunctionCall(self.repo.update, newbook)
        functionUndo = FunctionCall(self.repo.update, original_state)
        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))

    def find_book_by_title(self, title):
        title = title.lower()
        matching_books = []
        for book in self.repo.get_all_books():
            if title in book.title.lower():
                matching_books.append(book)
        return matching_books

    def find_book_by_author(self, author):
        author = author.lower()
        matching_books = []
        for book in self.repo.get_all_books():
            if author in book.author.lower():
                matching_books.append(book)
        return matching_books

    def find_book_by_id(self, book_id):
        for book in self.repo.get_all_books():
            if book.id == book_id:
                return book

    def get(self, key):
        for book in self.repo.get_all_books():
            if book.id == key:
                return book

    def get_author(self, key):
        for book in self.repo.get_all_books():
            if book.author == key:
                return book.author

    def generate_books(self):
        authors = ["Marissa Meyer", "Brandon Sanderson", "J. K Rowling", "M. L. Rio", "Donna Tartt", "Oscar Wilde",
                   "Ava Reid", "Gabrielle Zevin", "Stephanie Garber", "Cassandra Clare", "Emily Bronte",
                   "Charlotte Bronte", "Charles Dickens", "Jane Austen", "Holly Black", "J. R. R. Tolkien"]
        titles = ["Heartless", "Trees and the Emerald Sea", "The Prisoner of Azkaban", "If we were villains",
                  "Tomorrow Tomorrow and Tomorrow", "The Secret History", "Once upon a broken heart", "Chain of Gold",
                  "A study in Drowning", "Lord of the Rings", "The picture of Dorian Gray", "Jane Eyre",
                  "Wuthering Heights", "The Cruel Prince"]

        books_list = []
        generated_ids = set()
        i = 0

        while i < 20:
            try:
                book_id = randint(1000, 2000)
                if book_id in generated_ids:
                    continue
                author = authors[randint(0, len(authors) - 1)]
                title = titles[randint(0, len(titles) - 1)]
                book = Book(book_id, title, author)
                self.repo.add(book)
                generated_ids.add(book_id)
                books_list.append(book)
                i += 1
            except Exception as e:
                print(f"Error: {e}")
        return books_list



