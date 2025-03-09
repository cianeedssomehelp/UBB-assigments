
class Book:
    def __init__(self, isbn, author, title):
        if not isinstance(isbn, str):
            raise ValueError("isbn must be a string")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("author must be a string")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a string")
        self.__isbn = isbn
        self.__author = author.strip()
        self.__title = title.strip()

    def get_Author(self):
        return self.__author

    def get_Title(self):
        return self.__title

    def get_Isbn(self):
        return self.__isbn

    def set_Isbn(self, new_isbn):
        self.__isbn = new_isbn

    def set_Author(self, new_author):
        self.__author = new_author

    def set_Title(self, new_title):
        self.__title = new_title

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.__isbn, self.__author, self.__title) == (other.__isbn, self.__author, self.__title)
        return False

    def __str__(self):
        return f"Isbn: {self.__isbn}, Author: {self.__author}, Title: {self.__title}"

