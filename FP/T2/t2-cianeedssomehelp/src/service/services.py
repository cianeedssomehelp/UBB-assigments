from src.repository.memoryrepo import DriverMemory, AddressMemory


class DriverServices:
    def __init__(self, repo):
        self.repo = repo

    def sort_by_name(self):
        for i in range (0, len(self.repo.get_all_drivers())-1):
            for j in range (i + 1, len(self.repo.get_all_drivers())):
                if self.repo.get_all_drivers()[i].name > self.repo.get_all_drivers()[j].name:
                    self.repo.get_all_drivers()[j], self.repo.get_all_drivers()[i] = self.repo.get_all_drivers()[i], self.repo.get_all_drivers()[j]


class AddressServices:
    def __init__(self, repo):
        self.repo = repo

    def sort_by_name(self):
        for i in range(0, len(self.repo.get_all_addresses()) - 1):
            for j in range(i + 1, len(self.repo.get_all_addresses())):
                if self.repo.get_all_addresses()[i].name > self.repo.get_all_addresses()[j].name:
                    self.repo.get_all_addresses()[j], self.repo.get_all_addresses()[i] = self.repo.get_all_addresses()[i], self.repo.get_all_addresses()[j]


    def list_of_drivers_near_address(self, address):
        drivers = self.repo.get_all_drivers()
        distance = []
        i = 0
        for driver in drivers:
            distance[i] = abs(address.x - driver.x) + abs(address.y - driver.y)
            i = i + 1
        for i in range(0, len(drivers) - 1):
            for j in range(i + 1, len(drivers)):
                if distance[i] > distance[j]:
                    distance[i], distance[j] = distance[j], distance[i]
                    drivers[i], drivers[j] = drivers[j], drivers[i]



