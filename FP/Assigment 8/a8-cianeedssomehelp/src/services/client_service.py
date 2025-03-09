from random import randint
from faker import Faker
from src.repository.repoMemory import ClientRepo
from src.domain.client import Client
from src.domain.bookandclientvalidators import ClientsValidator

class ClientServices:
    def __init__(self, repo: ClientRepo, rentals_repo, clientsValidator: ClientsValidator):
        self.repo = repo
        self.rentals_repo = rentals_repo
        self.__clientsValidator = clientsValidator

    def add_client(self, client_id, name):
        for client in self.repo.get_all_clients():
            if client.id == client_id:
                return False
        try:
            client = Client(client_id, name)
            self.__clientsValidator.validate_clients(client)
            self.repo.add(client)
            return True
        except (ValueError , TypeError):
            return False

    def remove_client(self, client_id):
        for existing_client in self.repo.get_all_clients():
            if existing_client.id == client_id:
                self.repo.remove(existing_client)
        rentals_to_remove = [rental for rental in self.rentals_repo.get_all_rentals() if rental.client.id == client_id]
        for rental in rentals_to_remove:
            self.rentals_repo.remove(rental)

    def update_client(self, client_id, name):
        for client in self.repo.get_all_clients():
            if client.id == client_id:
                client.set_name(name)

    def find_client_by_name(self, client_name):
        client_name = client_name.lower()
        matching_clients = []
        for client in self.repo.get_all_clients():
            if client_name in client.name.lower():
                matching_clients.append(client)
        return matching_clients

    def find_client_by_id(self, client_id):
        for client in self.repo.get_all_clients():
            if client.id == client_id:
                return client

    def generate_clients(self):
        fake = Faker()
        clients_list = []
        i = 0
        while i < 20:
            try:
                client_id = int(randint(100, 200))
                client_name = fake.name()
                client = Client(client_id, client_name)
                self.repo.add(client)
                clients_list.append(client)
                i += 1
            except Exception as e:
                print(e)
        return clients_list






