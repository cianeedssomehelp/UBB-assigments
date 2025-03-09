from src.repository.repoMemory import *
from src.domain.book import *
class Services:
    def __init__(self, repo: BookMemoryRepo):
        self.repo = repo

    def add_book(self, isbn, author, title):
        """
        A function that adds a new book entity to the repository.
        :param isbn: isbn of the book
        :param author: author of the book
        :param title: title of the book
        :return: the new updated list of book entities
        """
        for book in self.repo.get_all_books():
            if book.get_Isbn() == isbn:
                return False
        try:
            book = Book(isbn, author, title)
            self.repo.add_book(book)
            return True
        except ValueError or TypeError:
            return False

    def filter_books(self, wordfromtitle):
        """
        A function that filters books based on a word. If the title of the book starts with the given word then that book is deleted from the list.
        :param wordfromtitle: a supposed first word from the title of the book entered by the user
        :return: the list of books without the book that has a title starting with the given word
        """
        if wordfromtitle == "":
            raise ValueError("You must enter a word.")
        books = self.repo.get_all_books()
        books_to_remove = [b for b in books if b.get_Title().split()[0] != wordfromtitle]
        self.repo.clear()
        for book in books_to_remove:
            self.repo.add_book(book)

    def undo_operations(self, history):
        """
        A function that undoes the operations of the repository.
        :param history: all the ways the list has been changed since starting the program
        :return: the previous state of the repository
        """
        if len(history) == 0:
            print("No undo available.")
            return
        previous_state = history.pop()
        self.repo.clear()
        for book in previous_state:
            self.repo.add_book(book)
        print("The undo was successful.")




