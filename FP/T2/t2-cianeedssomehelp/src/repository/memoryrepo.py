class DriverMemory:
    def __init__(self):
        self._data = []

    def get_all_drivers(self):
        return self._data

    def get_driver(self, driver_name):
        for driver in self._data:
            if driver.driver_name == driver_name:
                return driver

class AddressMemory:
    def __init__(self):
        self._data = []

    def get_all_addresses(self):
        return self._data

    def get_address(self, id):
        for address in self._data:
            if address.address_id == id:
                return address
