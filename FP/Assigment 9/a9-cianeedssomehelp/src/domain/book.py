import pickle


class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.__id = book_id
        self.__author = author
        self.__title = title

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def id(self):
        return self.__id

    def set_book_id(self, new_id):
        self.__id = new_id

    def set_author(self, new_author):
        self.__author = new_author

    def set_title(self, new_title):
        self.__title = new_title

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.id == other.id and self.title == other.title and self.author == other.author
        return False

    def __hash__(self):
        return hash((self.id, self.title, self.author))

    def __str__(self):
        return f"Id: {self.__id}, Title: {self.__title}, Author: {self.__author}"
