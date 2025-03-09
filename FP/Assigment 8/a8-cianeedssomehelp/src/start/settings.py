class Settings:
    def __init__(self, file_name):
        self._file_name = file_name

    def get_repository(self):
        try:
            with open(self._file_name, "r") as file:
                repository_line = file.readline()
            parts = repository_line.strip().split(" ")
            if len(parts) > 3:
                raise ValueError("Invalid settings file format. Could not find repository.")
            repository = parts[2]
            repository = repository[1:-1]
            return repository
        except FileNotFoundError:
            raise ValueError("Settings file not found.")

    def get_book_repository(self):
        with open(self._file_name, "r") as file:
            _ = file.readline()
            repository_line = file.readline()
        book_repository = repository_line.strip().strip('"').split(" ")[2]
        book_repository = book_repository[1:-1]
        return book_repository

    def get_client_repository(self):
        with open(self._file_name, "r") as file:
            _ = file.readline()
            repository_line = file.readline()
        client_repository = repository_line.strip().strip('"').split(" ")[2]
        client_repository = client_repository[1:-1]
        return client_repository

    def get_rental_repository(self):
        with open(self._file_name, "r") as file:
            _ = file.readline()
            repository_line = file.readline()
        rental_repository = repository_line.strip().strip('"').split(" ")[2]
        rental_repository = rental_repository[1:-1]
        return rental_repository
