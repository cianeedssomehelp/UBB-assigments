from random import randint
from src.repository.repoMemory import BookRepo
from src.domain.book import Book
from src.domain.bookandclientvalidators import BookValidator


class BookServices:
    def __init__(self, repo: BookRepo, rental_repo, bookValidator: BookValidator):
        self.repo = repo
        self.rentals_repo = rental_repo
        self.__bookValidator = bookValidator

    def add_book(self, book_id, title, author):
        for book in self.repo.get_all_books():
            if book.id == book_id:
                return False
        try:
            book = Book(book_id, title, author)
            self.__bookValidator.validate_book(book)
            self.repo.add(book)
            return True
        except ValueError or TypeError:
            return False

    def remove_book(self, book_id):
        for existing_book in self.repo.get_all_books():
            if existing_book.id == book_id:
                self.repo.remove(existing_book)
        rentals_to_remove = [rental for rental in self.rentals_repo.get_all_rentals() if rental.book.id == book_id]
        for rental in rentals_to_remove:
            self.rentals_repo.remove(rental)


    def update_book(self, book_id, title, author):
        for book in self.repo.get_all_books():
            if book.id == book_id:
                book.set_title(title)
                book.set_author(author)

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
        pass

    def generate_books(self):
        authors = ["Marissa Meyer", "Brandon Sanderson", "J. K Rowling", "M. L. Rio", "Donna Tartt", "Oscar Wilde",
                   "Ava Reid", "Gabrielle Zevin", "Stephanie Garber", "Cassandra Clare", "Emily Bronte",
                   "Charlotte Bronte", "Charles Dickens", "Jane Austen", "Holly Black", "J. R. R. Tolkien"]
        titles = ["Heartless", "Trees and the Emerald Sea", "The Prisoner of Azkaban", "If we were villains",
                  "Tomorrow Tomorrow and Tomorrow", "The Secret History", "Once upon a broken heart", "Chain of Gold",
                  "A study in Drowning", "Lord of the Rings", "The picture of Dorian Gray", "Jane Eyre",
                  "Wuthering Heights", "The Cruel Prince"]
        books_list = []
        i = 0
        while i < 20:
            try:
                book_id = int(randint(1000, 2000))
                author = authors[randint(0, len(authors) - 1)]
                title = titles[randint(0, len(titles) - 1)]
                book = Book(book_id, title, author)
                self.add_book(book_id, title, author)
                books_list.append(book)
                i += 1
            except Exception as e:
                print(e)
        return books_list





