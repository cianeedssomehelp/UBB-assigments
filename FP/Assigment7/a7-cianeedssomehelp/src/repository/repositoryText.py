from src.repository.repoMemory import BookMemoryRepo
from src.domain.book import *
from copy import deepcopy

class RepositoryError(Exception):
    pass

class BookTextFileRepo(BookMemoryRepo):
    def __init__(self):
        self.__filename = "books.txt"
        self._data = []
        self._history = []
        if self.load_file():
            self._history.append(deepcopy(self._data))
        else:
            super().__init__()

    def load_file(self):
        """
        Loads the books into a text file.
        """
        try:
            fin = open(self.__filename, "rt")
            lines = fin.readlines()
            fin.close()
        except IOError:
            return False
        for line in lines:
            if line == "":
                continue
            line = line.strip()
            line = line.split(",")
            book = Book(line[0], line[1], line[2])
            self._data.append(book)
        if len(super().get_all_books()) == 0:
            return False
        return True

    def __saveFile(self):
        """
        Saves the books into a text file.
        """
        try:
            fout = open(self.__filename, "wt")
            books = super().get_all_books()
            for book in books:
                book_string = str(book.get_Isbn()) + "," + str(book.get_Author()) + "," + str(book.get_Title()) + '\n'
                fout.write(book_string)
        except IOError:
            raise RepositoryError("Save file not found.")

    def add_book(self, book):
        """
        This function adds a book to the repository.
        :param book: our book
        :return: the new list of books
        """
        super().add_book(book)
        self.__saveFile()