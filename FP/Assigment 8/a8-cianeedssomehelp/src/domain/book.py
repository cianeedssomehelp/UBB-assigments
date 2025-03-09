class Book:
    def __init__(self, book_id: int, title: str, author: str):
        if not isinstance(book_id, int):
            raise ValueError("id must be an integer")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("author must be a string")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a string")
        self.__id = book_id
        self.__author = author.strip()
        self.__title = title.strip()

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
            return (self.__id, self.__title, self.__author) == (other.__id, self.__title, self.__author)
        return False

    def __str__(self):
        return f"Id: {self.__id}, Title: {self.__title}, Author: {self.__author}"