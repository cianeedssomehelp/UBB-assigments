from src.services.services import Services

from copy import deepcopy
from random import randint, choices
import string



class UI:
    def __init__(self, service: Services):
        self.service = service

    @staticmethod
    def print_menu():
        print("What would you like to do?")
        print("0. Exit the program.")
        print("1. Add a book.")
        print("2. Display the list of books.")
        print("3. Filter the list of books.")
        print("4. Undo the last operation.")

    def add_book_ui(self):
        try:
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            if self.service.add_book(isbn, author, title):
                print("\nBook added successfully!\n")
                return True
            else:
                print("\nBook could not be added!\n")
                return False
        except ValueError or TypeError:
            print("Invalid input! Please enter valid data!")
            return False

    def display_books(self):
        books = self.service.repo.get_all_books()
        if not books:
            print("No books found!")
        else:
            for book in books:
                print(str(book))
            print()

    def filter_books_ui(self):
        try:
            word_from_title = input("Enter the first word from the title of the book: ")
            self.service.filter_books(word_from_title)
            print("Books filtered successfully!")
            return True
        except ValueError:
            print("Invalid input! Please enter valid data!")
            return False

    def undo_operation_(self, history):
        self.service.undo_operations(history)

    def generate_books(self):
        i = 0
        authors = ["Marissa Meyer", "Brandon Sanderson", "J. K Rowling", "M. L. Rio", "Donna Tartt", "Oscar Wilde",
                   "Ava Reid", "Gabrielle Zevin", "Stephanie Garber", "Cassandra Clare", "Emily Bronte",
                   "Charlotte Bronte", "Charles Dickens", "Jane Austen", "Holly Black", "J. R. R. Tolkien"]
        titles = ["Heartless", "Trees and the Emerald Sea", "The Prisoner of Azkaban", "If we were villains",
                  "Tomorrow Tomorrow and Tomorrow", "The Secret History", "Once upon a broken heart", "Chain of Gold",
                  "A study in Drowning", "Lord of the Rings", "The picture of Dorian Gray", "Jane Eyre",
                  "Wuthering Heights", "The Cruel Prince"]
        while i < 10:
            isbn = ''.join(choices(string.digits, k=5))
            author = authors[randint(0, len(authors) - 1)]
            title = titles[randint(0, len(titles) - 1)]
            if self.service.add_book(isbn, author, title):
                i += 1
            else:
                print(f"Failed to add book: {isbn}")

    def start(self, history: list):
        if self.service.repo.get_all_books() == []:
            self.generate_books()
        while True:
            UI.print_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice < 0:
                    raise ValueError("The input of your choice should not be a negative number.")
                elif choice > 4:
                    raise ValueError("You've only got choices from 0 to 4!")
                elif choice == 0:
                    print("Thank you for your time!")
                    break
                elif choice == 1:
                    history.append(deepcopy(self.service.repo.get_all_books()))
                    if not self.add_book_ui():
                        history.pop()
                elif choice == 2:
                    self.display_books()
                elif choice == 3:
                    history.append(deepcopy(self.service.repo.get_all_books()))
                    if not self.filter_books_ui():
                        history.pop()
                elif choice == 4:
                    self.undo_operation_(history)
                else:
                    raise ValueError("Invalid input")
            except Exception as e:
                print(e)