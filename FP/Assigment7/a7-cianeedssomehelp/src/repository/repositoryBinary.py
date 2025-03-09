
from src.repository.repoMemory import BookMemoryRepo
import pickle

class BinaryFileRepository(BookMemoryRepo):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def add_book(self, entity):
        """
        This method adds a book to the repository.
        :param entity: the book
        :return: the new list of books
        """
        books = self.get_all_books()
        books.append(entity)
        self._write_all(books)

    def remove_book(self, entity):
        """
        This method removes a book from the repository.
        :param entity: book
        :return: the new list of books
        """
        books = self.get_all_books()
        books = [b for b in books if b != entity]
        self._write_all(books)

    def get_all_books(self):
        """
        This method returns a list of all books in the repository.
        :return: the list of books
        """
        try:
            with open(self._filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def clear(self):
        """
        This method clears the repository.
        :return: fresh clean repository
        """
        self._write_all([])

    def _write_all(self, books):
        """
        This method writes all the books in the repository file.
        :param books: the list of books
        """
        with open(self._filename, 'wb') as file:
            pickle.dump(books, file)
