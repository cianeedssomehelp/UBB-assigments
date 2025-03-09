from src.repository.repository import DriverTextFile, AddressTextFile
from src.service.services import DriverServices, AddressServices
from src.ui.ui import UI

def main():
    driver_repo = DriverTextFile()
    address_repo = AddressTextFile()

    driver_services = DriverServices(driver_repo)
    address_services = AddressServices(address_repo)

    ui = UI(driver_services, address_services)
    ui.start()


if __name__ == '__main__':
    main()