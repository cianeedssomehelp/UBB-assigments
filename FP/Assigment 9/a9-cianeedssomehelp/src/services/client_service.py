from copy import deepcopy
from random import randint
from faker import Faker
from src.repository.repoMemory import ClientRepo
from src.domain.client import Client
from src.domain.bookandclientvalidator import ClientsValidator
from src.services.undo_service import FunctionCall, Operation, CascadedOperation

class ClientServices:
    def __init__(self, repo: ClientRepo, rentals_repo, clientsValidator: ClientsValidator, undo_service):
        self.repo = repo
        self.rentals_repo = rentals_repo
        self.__clientsValidator = clientsValidator
        self._undo_service = undo_service

    def add_client(self, client_id, name):
        client = Client(client_id, name)
        self.__clientsValidator.validate_clients(client)
        self.repo.add(client)

        functionRedo = FunctionCall(self.repo.add, client)
        functionUndo = FunctionCall(self.repo.remove, client.id)

        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))
        return client

    def remove_client(self, client_id):
        rentals_to_remove = [
            rental for rental in self.rentals_repo.get_all_rentals()
            if rental.client.id == client_id
        ]

        for rental in rentals_to_remove:
            self.rentals_repo.remove(rental.id)  # Use rental ID explicitly

        client = self.repo.remove(client_id)

        functionRedo = FunctionCall(self.repo.remove, client_id)
        functionUndo = FunctionCall(self.repo.add, client)
        operations = [Operation(functionUndo, functionRedo)]

        for rental in rentals_to_remove:
            functionRedo = FunctionCall(self.rentals_repo.remove, rental.id)
            functionUndo = FunctionCall(self.rentals_repo.add, rental)
            operations.append(Operation(functionUndo, functionRedo))

        self._undo_service.recordUndo(CascadedOperation(*operations))

    def update_client(self, client_id, name):
        original_client = self.repo.get_client(client_id)
        if original_client is None:
            raise ValueError("Client not found.")

        original_state = deepcopy(original_client)
        for client in self.repo.get_all_clients():
            if client.id == client_id:
                client.set_name(name)

        newclient = Client(client_id, name)
        functionRedo = FunctionCall(self.repo.update, newclient)
        functionUndo = FunctionCall(self.repo.update, original_state)
        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))

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

    def get(self, key):
        for client in self.repo.get_all_clients():
            if client.id == key:
                return client

    def generate_clients(self):
        fake = Faker()
        clients_list = []
        generated_ids = set()
        i = 0
        while i < 20:
            try:
                client_id = int(randint(100, 200))
                if client_id in generated_ids:
                    continue
                client_name = fake.name()
                client = Client(client_id, client_name)
                self.repo.add(client)
                generated_ids.add(client_id)
                clients_list.append(client)
                i += 1
            except Exception as e:
                print(e)
        return clients_list






