from src.services.book_service import BookServices
from src.services.client_service import ClientServices
from src.services.rental_service import RentalService
from src.domain.book import Book
from src.domain.client import Client
from src.repository.repoMemory import BookRepo, RentalRepo, ClientRepo
from datetime import date, timedelta
from random import randint
from src.services.undo_service import UndoService


class UI:
    def __init__(self, book_service: BookServices, client_service: ClientServices, rental_service: RentalService, undo_service):
        self.book_service = book_service
        self.client_service = client_service
        self.rental_service = rental_service
        self.undo_service = undo_service

        pass
    @staticmethod
    def print_Menu():
        print("What would you like to do?")
        print("1. Play with books. ")
        print("2. Play with clients. ")
        print("3. Rent someone a book. ")
        print("4. Most rented books.")
        print("5. Most active clients.")
        print("6. Most rented author.")
        print("0. Exit the application.")

    @staticmethod
    def print_Books():
        print("Here's what you can do with books: ")
        print("1. Display the current list of books.")
        print("2. Add a new book.")
        print("3. Remove a book.")
        print("4. Search for a book.")
        print("5. Update a book.")
        print("6. Undo.")
        print("7. Redo.")
        print("0. Go back to the main menu.")

    @staticmethod
    def print_Clients():
        print("Here's what you can do with clients: ")
        print("1. Display the current list of clients.")
        print("2. Add a new client.")
        print("3. Remove a client.")
        print("4. Search for a client.")
        print("5. Update a client.")
        print("6. Undo.")
        print("7. Redo.")
        print("0. Go back to the main menu.")

    @staticmethod
    def print_rental():
        print("Here's what you can do: ")
        print("1. Display the current rentals.")
        print("2. Rent someone a book.")
        print("3. Return a book.")
        print("4. Undo.")
        print("5. Redo.")
        print("0. Go back to the main menu.")

    def add_book_ui(self):
        try:
            book_id = int(randint(2000, 3000))
            title = input("Enter title: ")
            author = input("Enter author: ")
            if self.book_service.add_book(book_id, title, author):
                print("\nBook added successfully!\n")
                return True
            else:
                print("\nBook could not be added!\n")
                return False
        except ValueError or TypeError:
            print("Invalid input! Please enter valid data!")
            return False

    def remove_book_ui(self):
        try:
            book_id = int(input("Enter book id: "))
            self.book_service.remove_book(book_id)
            print("Book deleted successfully!\n")
            return True
        except ValueError:
            print("Invalid input! Please enter valid data!")
            return False

    def update_book_ui(self):
        try:
            book_id = int(input("Enter book id: "))
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            self.book_service.update_book(book_id, new_title, new_author)
            print("Book updated successfully!\n")
            return True
        except ValueError:
            print("Invalid input! Please enter valid data!")
            return False

    def find_book_by_id_ui(self):
        try:
            book_id = int(input("Enter book id: "))
            book = self.book_service.find_book_by_id(book_id)
            print(f"Here's your book: {str(book)}! \n")
        except ValueError:
            print("Invalid input! Please enter valid data!")

    def find_book_by_title_ui(self):
        try:
            book_title = input("Enter book title: ")
            books = self.book_service.find_book_by_title(book_title)

            if books:
                print("Here are the books matching your search: ")
                for book in books:
                    print(f"- {str(book)}")  # Printing each book in the list
            else:
                print("No books found with that title.")
        except ValueError:
            print("Invalid input! Please enter valid data!")

    def find_book_by_author_ui(self):
        try:
            book_author = input("Enter book author: ")
            books = self.book_service.find_book_by_author(book_author)

            if books:
                print("Here are the books matching your search: ")
                for book in books:
                    print(f"- {str(book)}")
            else:
                print("No books found by that author.")
        except ValueError:
            print("Invalid input! Please enter valid data!")

    def display_books(self):
        books = self.book_service.repo.get_all_books()
        if not books:
            print("No books found!")
        else:
            for book in books:
                print(str(book))
            print()

    def add_client_ui(self):
        try:
            client_id = int(randint(200, 300))
            client_name = input("Enter client name: ")
            if self.client_service.add_client(client_id, client_name):
                print("\nClient added successfully!\n")
                return True
            else:
                print("\nClient could not be added!\n")
                return False
        except ValueError or TypeError:
            print("Invalid input! Please enter valid data!")
            return False

    def remove_client_ui(self):
        try:
            client_id = int(input("Enter client id: "))
            self.client_service.remove_client(client_id)
            print("Client removed successfully!\n")
        except (ValueError, TypeError):
            print("Invalid input! Please enter valid data!")

    def update_client_ui(self):
        try:
            client_id = int(input("Enter client id: "))
            new_name = input("Enter new name: ")
            self.client_service.update_client(client_id, new_name)
            print("Client updated successfully!\n")
            return True
        except ValueError or TypeError:
            print("Invalid input! Please enter valid data!")
            return False

    def find_client_by_id_ui(self):
        try:
            client_id = int(input("Enter client id: "))
            client = self.client_service.find_client_by_id(client_id)
            print(f"Here's your client: {str(client)}! \n")
        except ValueError:
            print("Invalid input! Please enter valid data!")

    def find_client_by_name_ui(self):
        try:
            client_name = input("Enter client name: ")
            clients = self.client_service.find_client_by_name(client_name)

            if clients:
                print("Here are the clients matching your search: ")
                for client in clients:
                    print(f"- {str(client)}")
            else:
                print("No clients found with that name.")
        except ValueError:
            print("Invalid input! Please enter valid data!")


    def display_clients(self):
        clients = self.client_service.repo.get_all_clients()
        if not clients:
            print("No clients found!")
        else:
            for client in clients:
                print(str(client))
            print()

    def rent_book_ui(self):
        try:
            rental_id = int(randint(70, 90))
            client_id = int(input("Enter client ID: "))
            book_id = int(input("Enter book ID: "))
            rental_date = date.today()
            day = randint(5, 30)
            stop_date = rental_date + timedelta(days = day)
            self.rental_service.add(rental_id, stop_date, rental_date, self.client_service.find_client_by_id(client_id), self.book_service.find_book_by_id(book_id))
            print("Book rented successfully!\n")
        except Exception as e:
            print(f"Error: {e}")

    def return_book_ui(self):
        try:
            rental_id = int(input("Enter rental ID: "))
            if rental_id < 50 or rental_id > 70:
                raise ValueError("Please make sure the rental Id you entered is a valid one! (between 50 and 70)")
            self.rental_service.remove(rental_id)
            print("Book returned successfully!\n")
        except ValueError as ve:
            print(ve)

    def display_rentals(self):
        rentals = self.rental_service.repo.get_all_rentals()
        if not rentals:
            print("No rentals found!")
        else:
            for rental in rentals:
                print(str(rental))
            print()

    def most_rented_books(self):
        books = self.rental_service.statistics_by_most_rented_books()
        print("Here are the most rented books: ")
        if not books:
            print("No books found!")
        else:
            for book in books:
                print(str(book))
            print()

    def most_active_clients(self):
        clients = self.rental_service.statistics_by_most_active_clients()
        print("Here are the most active clients: ")
        if not clients:
            print("No clients found!")
        else:
            for client in clients:
                print(str(client))
            print()

    def most_rented_authors(self):
        authors = self.rental_service.statistics_by_most_rented_author()
        print("Here are the most rented authors: ")
        if not authors:
            print("No authors found!")
        else:
            for author in authors:
                print(str(author))
            print()

    def undo_ui(self):
        try:
            self.undo_service.undo()
            print("Undo successful!\n")
        except Exception as e:
            print(f"Error: {e}")

    def redo_ui(self):
        try:
            self.undo_service.redo()
            print("Redo successful!\n")
        except Exception as e:
            print(f"Error: {e}")

    def start(self):
        if not self.book_service.repo.get_all_books():
            self.book_service.generate_books()

        if not self.client_service.repo.get_all_clients():
            self.client_service.generate_clients()

        if not self.rental_service.repo.get_all_rentals():
            self.rental_service.generate_rentals(self.book_service.repo.get_all_books(), self.client_service.repo.get_all_clients())
        while True:
            UI.print_Menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    print("Thank you for using this program!")
                    break
                elif choice == 1:
                    go_on = True
                    while go_on:
                        UI.print_Books()
                        choose = int(input("Enter your choice: "))
                        if choose == 1:
                            self.display_books()
                        elif choose == 2:
                            self.add_book_ui()
                        elif choose == 3:
                            self.remove_book_ui()
                        elif choose == 4:
                            option = input("Do you want to find the book by the id, the title or the author?: ")
                            if option == 'id':
                                self.find_book_by_id_ui()
                            elif option == 'title':
                                self.find_book_by_title_ui()
                            elif option == 'author':
                                self.find_book_by_author_ui()
                            else:
                                raise ValueError("Invalid input! Please enter a valid option: id, title or author!")
                        elif choose == 5:
                            self.update_book_ui()
                        elif choose == 6:
                            self.undo_ui()
                        elif choose == 7:
                            self.redo_ui()
                        elif choose == 0:
                            go_on = False
                        else:
                            raise ValueError("Invalid input! Please enter a valid option between 0 and 7"
                                             "!")
                elif choice == 2:
                    go_on = True
                    while go_on:
                        UI.print_Clients()
                        choose = int(input("Enter your choice: "))
                        if choose == 1:
                            self.display_clients()
                        elif choose == 2:
                            self.add_client_ui()
                        elif choose == 3:
                            self.remove_client_ui()
                        elif choose == 4:
                            option = input("Do you want to find the client by the id or by their name?: ")
                            if option == "id":
                                self.find_client_by_id_ui()
                            elif option == "name":
                                self.find_client_by_name_ui()
                            else:
                                raise ValueError("Invalid input! Please enter a valid option between id and name!")
                        elif choose == 5:
                            self.update_client_ui()
                        elif choose == 6:
                            self.undo_ui()
                        elif choose == 7:
                            self.redo_ui()
                        elif choose == 0:
                            go_on = False
                        else:
                            raise ValueError("Invalid input! Please enter a valid option between 0 and 7!")
                elif choice == 3:
                    go_on = True
                    while go_on:
                        UI.print_rental()
                        option = int(input("Enter your choice: "))
                        if option == 1:
                            self.display_rentals()
                        elif option == 2:
                            self.rent_book_ui()
                        elif option == 3:
                            self.return_book_ui()
                        elif option == 4:
                            self.undo_ui()
                        elif option == 5:
                            self.redo_ui()
                        elif option == 0:
                            go_on = False
                        else:
                            raise ValueError("Invalid input! Please enter a valid option between 0 and 5!")
                elif choice == 4:
                    self.most_rented_books()
                elif choice == 5:
                    self.most_active_clients()
                elif choice == 6:
                    self.most_rented_authors()
                else:
                    print("Invalid input! Please make a choice from 0 to 6!")
            except Exception as e:
                print(e)