import unittest
from datetime import date, timedelta
from src.domain.bookandclientvalidators import BookValidator, ClientsValidator
from src.domain.rentalValidator import RentalValidator
from src.repository.repoMemory import BookRepo, ClientRepo, RentalRepo
from src.services.book_service import BookServices
from src.services.client_service import ClientServices
from src.services.rental_service import RentalService

class TestServicesAndRepos(unittest.TestCase):
    def setUp(self):
        self.book_repo = BookRepo()
        self.client_repo = ClientRepo()
        self.rental_repo = RentalRepo()

        self.book_validator = BookValidator()
        self.client_validator = ClientsValidator()
        self.rental_validator = RentalValidator()

        # Services
        self.book_service = BookServices(self.book_repo, self.rental_repo, self.book_validator)
        self.client_service = ClientServices(self.client_repo, self.rental_repo, self.client_validator)
        self.rental_service = RentalService(self.rental_repo, self.client_service, self.book_service, self.rental_validator)

    def test_add_book(self):
        book_id = 101
        title = "Test Book"
        author = "Test Author"

        result = self.book_service.add_book(book_id, title, author)
        self.assertTrue(result)

        book = self.book_repo.find_by_id(book_id)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)

    def test_remove_book(self):
        book_id = 102
        self.book_service.add_book(book_id, "To Remove", "Author")

        self.book_service.remove_book(book_id)
        with self.assertRaises(Exception) as context:
            self.book_repo.find_by_id(book_id)
        self.assertTrue("does not exist" in str(context.exception))

    def test_add_client(self):
        client_id = 201
        name = "Test Client"

        result = self.client_service.add_client(client_id, name)
        self.assertTrue(result)

        client = self.client_repo.find_by_id(client_id)
        self.assertIsNotNone(client)
        self.assertEqual(client.name, name)

    def test_remove_client(self):
        client_id = 202
        self.client_service.add_client(client_id, "To Remove")

        self.client_service.remove_client(client_id)
        with self.assertRaises(Exception) as context:
            self.client_repo.find_by_id(client_id)
        self.assertTrue("does not exist" in str(context.exception))

    def test_add_rental(self):
        book_id = 301
        client_id = 302
        rental_id = 401

        self.book_service.add_book(book_id, "Rental Book", "Author")
        self.client_service.add_client(client_id, "Rental Client")

        start_date = date(2025, 1, 1)
        end_date = start_date + timedelta(days=7)
        book = self.book_repo.find_by_id(book_id)
        client = self.client_repo.find_by_id(client_id)

        self.rental_service.add(rental_id, end_date, start_date, client, book)

        rental = self.rental_repo.get_rental(rental_id)
        self.assertIsNotNone(rental)
        self.assertEqual(rental.book.id, book_id)
        self.assertEqual(rental.client.id, client_id)

    def test_remove_rental(self):
        book_id = 303
        client_id = 304
        rental_id = 402

        self.book_service.add_book(book_id, "Another Rental Book", "Author")
        self.client_service.add_client(client_id, "Another Rental Client")

        start_date = date(2025, 1, 1)
        end_date = start_date + timedelta(days=7)
        book = self.book_repo.find_by_id(book_id)
        client = self.client_repo.find_by_id(client_id)

        self.rental_service.add(rental_id, end_date, start_date, client, book)
        self.rental_service.remove(rental_id)

        rental = self.rental_repo.get_rental(rental_id)
        self.assertIsNone(rental)

    def test_generate_books(self):
        books = self.book_service.generate_books()
        self.assertEqual(len(books), 20)
        self.assertEqual(len(self.book_repo.get_all_books()), 20)

    def test_generate_clients(self):
        clients = self.client_service.generate_clients()
        self.assertEqual(len(clients), 20)
        self.assertEqual(len(self.client_repo.get_all_clients()), 20)

    def test_generate_rentals(self):
        books = self.book_service.generate_books()
        clients = self.client_service.generate_clients()

        rentals = self.rental_service.generate_rentals(books, clients)
        self.assertGreaterEqual(len(rentals), 0)

if __name__ == "__main__":
    unittest.main()
