from copy import deepcopy

from src.domain.address import Address
from src.repository.memoryrepo import DriverMemory, AddressMemory
from src.service.services import DriverServices
from src.domain.driver import Driver


class DriverTextFile(DriverMemory):
    def __init__(self):
        self._filename = "drivers.txt"
        self._history = []
        self._data = []
        if self.__loadfile():
            self._history.append(deepcopy(self._data))
        else:
            super().__init__()

    def __loadfile(self):
        try:
            with open(self._filename, "rt") as fin:
                lines = fin.readlines()
        except IOError:
            print("Can't open file.")
        for line in lines:
            if line.strip() == "":
                continue
            line = line.strip()
            line = line.split(", ")
            new_driver = Driver((line[0]), int(line[1]), int(line[2]))
            self._data.append(new_driver)
        fin.close()
        if len(self._data) == 0:
            return False
        return True

    def __savefile(self):
        try:
            with open(self._filename, "wt") as fout:
                for driver in self._data:
                    driver_string = f"{driver.name}, {driver.x}, {driver.y}\n"
                    fout.write(driver_string)
            fout.close()
        except IOError as e:
            raise Exception(f"Error saving file: {str(e)}")


class AddressTextFile(AddressMemory):
    def __init__(self):
        self._filename = "address.txt"
        self._history = []
        self._data = []
        if self.__loadfile():
            self._history.append(deepcopy(self._data))
        else:
            super().__init__()

    def __loadfile(self):
        try:
            with open(self._filename, "rt") as fin:
                lines = fin.readlines()
        except IOError:
            print("Can't open file.")
        for line in lines:
            if line.strip() == "":
                continue
            line = line.strip()
            line = line.split(", ")
            new_address = Address(int(line[0]), (line[1]), int(line[2]), int(line[3]))
            self._data.append(new_address)
        fin.close()
        if len(self._data) == 0:
            return False
        return True

    def __savefile(self):
        try:
            with open(self._filename, "wt") as fout:
                for address in self._data:
                    address_string = f"{address.id}, {address.name}, {address.x}, {address.y}\n"
                    fout.write(address_string)
            fout.close()
        except IOError as e:
            raise Exception(f"Error saving file: {str(e)}")



