
from copy import deepcopy
from pdoc import pdoc
from src.domain.book import Book

class RepositoryError(Exception):
    pass

class BookMemoryRepo:
    def __init__(self):
        self._data = []
        self._history = [deepcopy(self._data)]

    def get_book(self, isbn: str):
        """
        This function will return a book object.
        :param isbn: the unique code by which the book is identified.
        :return: the book.
        """
        for book in self._data:
            if book.get_Isbn() == isbn:
                return book

    def add_book(self, book: Book):
        """
        This function will add a book to the repository.
        :param book: the object we want to add.
        :return: the new list of objects
        """
        for existing_book in self._data:
            if existing_book.get_Isbn() == book.get_Isbn():
                raise RepositoryError(f"Book with ISBN {book.get_Isbn()} already exists.")
        self._data.append(book)

    def remove_book(self, book: Book):
        """
        This function will remove a book from the repository.
        :param book: the object we want to remove.
        :return: the new list of books
        """
        self._data.remove(book)

    def add_to_history(self):
        """
        This function will add a book to the history.
        :return: the history of books
        """
        self._history.append(deepcopy(self._data))

    def undo(self):
        """
        this function undoes any operations we make
        :return: the last state of the repository
        """
        if len(self._history) > 1:
            self._history.pop()
            self._data = deepcopy(self._history[-1])
        else:
            raise RepositoryError("No operations to undo.")
    def get_all_books(self):
        """
        This function will get the list of all books.
        :return: the list of books
        """
        return self._data

    def __len__(self):
        return len(self._data)

    def clear(self):
        """
        This function will clear the repository.
        :return: fresh clean repository
        """
        self._data.clear()

if __name__ == "__main__":
    """
    Generate HTML documentation using the pdoc package
    """
    f = open("repo.html", "wt")
    f.write(pdoc("repoMemory.py"))
    f.write(pdoc("repositoryBinary.py"))
    f.write(pdoc("repositoryText.py"))
    f.close()