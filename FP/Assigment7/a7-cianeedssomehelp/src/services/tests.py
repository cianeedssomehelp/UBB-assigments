from services import Services
from src.repository.repoMemory import BookMemoryRepo
from src.repository.repositoryBinary import BinaryFileRepository
from src.domain.book import Book
import os
import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        # Temporary files for testing
        self.text_file = "test_books.txt"
        self.binary_file = "test_books.bin"

        # Ensure the test files are clean before each test
        if os.path.exists(self.text_file):
            os.remove(self.text_file)
        if os.path.exists(self.binary_file):
            os.remove(self.binary_file)

    def tearDown(self):
        # Clean up temporary files after tests
        if os.path.exists(self.text_file):
            os.remove(self.text_file)
        if os.path.exists(self.binary_file):
            os.remove(self.binary_file)

    def test_add_book_memory(self):
        repo = BookMemoryRepo()
        services = Services(repo)

        services.add_book("ISBN001", "Author One", "Title One")
        self.assertEqual(repo.get_all_books(), [Book("ISBN001", "Author One", "Title One")])

        services.add_book("ISBN002", "Author Two", "Title Two")
        self.assertEqual(repo.get_all_books(), [
            Book("ISBN001", "Author One", "Title One"),
            Book("ISBN002", "Author Two", "Title Two")
        ])


    def test_add_book_binaryfile(self):
        repo = BinaryFileRepository(self.binary_file)
        services = Services(repo)

        services.add_book("ISBN001", "Author One", "Title One")
        self.assertEqual(repo.get_all_books(), [Book("ISBN001", "Author One", "Title One")])

        services.add_book("ISBN002", "Author Two", "Title Two")
        self.assertEqual(repo.get_all_books(), [
            Book("ISBN001", "Author One", "Title One"),
            Book("ISBN002", "Author Two", "Title Two")
        ])

    def test_filter_books_memory(self):
        repo = BookMemoryRepo()
        services = Services(repo)

        services.add_book("ISBN001", "Author One", "Title One")
        services.add_book("ISBN002", "Author Two", "Another Title")

        services.filter_books("Title")
        self.assertEqual(repo.get_all_books(), [Book("ISBN002", "Author Two", "Another Title")])

    def test_undo_memory(self):
        repo = BookMemoryRepo()
        services = Services(repo)

        history = [[Book("ISBN001", "Author One", "Title One")]]
        services.undo_operations(history)
        self.assertEqual(repo.get_all_books(), [Book("ISBN001", "Author One", "Title One")])

    def test_undo_binaryfile(self):
        repo = BinaryFileRepository(self.binary_file)
        services = Services(repo)

        history = [[Book("ISBN001", "Author One", "Title One")]]
        services.undo_operations(history)
        self.assertEqual(repo.get_all_books(), [Book("ISBN001", "Author One", "Title One")])


if __name__ == '__main__':
    unittest.main()
