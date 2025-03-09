import pickle


class Client:
    def __init__(self, client_id: int, name: str):
        self.__id = client_id
        self.__name = name.strip()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def set_client_id(self, client_id):
        self.__id = client_id

    def set_name(self, name):
        self.__name = name

    def __eq__(self, other):
        if isinstance(other, Client):
            return (self.__id, self.__name) == (other.__id, self.__name)
        return False

    def __str__(self):
        return f"Id: {self.__id}, Name: {self.__name}"


