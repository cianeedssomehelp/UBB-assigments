from src.domain.address import Address
from src.service.services import DriverServices, AddressServices


class UI:
    def __init__(self, driver_services: DriverServices, address_services: AddressServices):
        self.driver_service = driver_services
        self.address_services = address_services


    def PrintMenu(self):
        print("What would you like to do?")
        print("1. Display all addresses and drivers.")
        print("2. Find drivers with address.")
        print("3. Closest driver.")
        print("0. Exit the application.")

    def display_address(self):
        addresses = self.address_services.repo.get_all_addresses()
        if not addresses:
            print("No addresses found.")
        else:
            for address in addresses:
                print(str(address))
            print()

    def display_drivers(self):
        drivers = self.driver_service.repo.get_all_drivers()
        if not drivers:
            print("No drivers found.")
        else:
            for driver in drivers:
                print(str(driver))
            print()

    def list_of_drivers_near_address_ui(self):
        try:
            address_id = int(input("Enter address ID: "))
            address = self.address_services.repo.get_address(address_id)
            sorted_drivers = self.list_of_drivers_near_address(address)
            return sorted_drivers
        except ValueError as ve:
            print(ve)

    def list_of_drivers_near_address(self, address):
        """
        A function that helps us find the drivers near an address and sorts them by distance to that address
        :param address: the address we are using to look for drivers
        :return:
        """
        drivers = self.driver_service.repo.get_all_drivers()
        distances = []
        i = 0
        for driver in drivers:
            distance = abs(address.x - driver.x) + abs(address.y - driver.y)
            distances.append((driver, distance))

        sorted_drivers = sorted(distances, key=lambda x: x[1])
        sorted_drivers_list = [driver for driver, i in sorted_drivers]
        return sorted_drivers_list

    def display_dv(self, array: list):
        for driver in array:
            print(str(driver))

    def close_driver(self):
        drivers = self.driver_service.repo.get_all_drivers()
        addresses = self.address_services.repo.get_all_addresses()
        closest_driver = []

        for address in addresses:
            closest_drivers = None
            min_distance = float("inf")
            for driver in drivers:
                distance = abs(address.x - driver.x) + abs(address.y - driver.y)
                if distance < min_distance:
                    min_distance = distance
                    closest_drivers = driver
            closest_driver.append((address, closest_drivers))

        return closest_driver



    def closest_driver_ui(self):
        try:
            drivers = self.close_driver()
            for address, driver in drivers:
                print(str(address), str(driver))
        except ValueError as ve:
            print(ve)

    def start(self):
        while True:
            try:
                driver = []
                self.PrintMenu()
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.driver_service.sort_by_name()
                    self.address_services.sort_by_name()
                    self.display_address()
                    self.display_drivers()
                elif choice == 2:
                    self.display_dv(self.list_of_drivers_near_address_ui())
                elif choice == 3:
                    self.closest_driver_ui()
                elif choice == 0:
                    print("Thank you")
                    break
                else:
                    print("Invalid choice")
            except ValueError as ve:
                print(ve)
