from src.start.settings import Settings
from src.repository.repoMemory import RentalRepo, BookRepo, ClientRepo
from src.repository.repoBinaryFile import BookBinaryFileRepository, RentalsBinaryFileRepository, ClientBinaryFileRepository
from src.repository.repoTextFile import BookTextFileRepo, RentalTextFileRepo, ClientTextFileRepo
from src.services.book_service import BookServices
from src.services.client_service import ClientServices
from src.services.rental_service import RentalService
from src.ui.ui import UI
from src.domain.rentalValidator import RentalValidator
from src.domain.bookandclientvalidators import BookValidator, ClientsValidator


def main():
    settings = Settings("setting.properties")

    if settings.get_repository() == "repoMemory":
        books_repository = BookRepo()
        clients_repository = ClientRepo()
        rentals_repository = RentalRepo()
    elif settings.get_repository() == "repoBinaryFile":
        books_repository = BookBinaryFileRepository()
        clients_repository = ClientBinaryFileRepository()
        rentals_repository = RentalsBinaryFileRepository()
    elif settings.get_repository() == "repoTextFile":
        books_repository = BookTextFileRepo()
        clients_repository = ClientTextFileRepo()
        rentals_repository = RentalTextFileRepo(BookTextFileRepo(), ClientTextFileRepo())
    else:
        raise ValueError("Invalid repository.")

    book_services_repo = BookServices(books_repository, rentals_repository, BookValidator())
    client_services_repo = ClientServices(clients_repository, rentals_repository, ClientsValidator())
    rental_validator = RentalValidator()
    rental_service_repo = RentalService(rentals_repository, client_services_repo, book_services_repo, rental_validator)
    ui = UI(book_services_repo, client_services_repo, rental_service_repo)
    ui.start()

if __name__ == "__main__":
    main()