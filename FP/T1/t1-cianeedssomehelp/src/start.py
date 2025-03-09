from ui import *

def start():
    flights_list = [
        {"code": "100A", "duration": 30, "departure_city": "Barcelona", "destination": "Cluj-Napoca"},
        {"code": "101B", "duration": 40, "departure_city": "Bucuresti", "destination": "Rome"},
        {"code": "103C", "duration": 50, "departure_city": "Bucuresti", "destination": "Paris"}
    ]
    while True:
        printMenu()
        try:
            choice = int(input("Enter your choice:"))
            if choice < 0:
                raise ValueError("Choice should be positive.")
            elif choice > 5:
                raise ValueError("Choice should be less than 5.")
            elif choice == 0:
                print("Thank you for using this program.")
                break
            elif choice == 1:
                try:
                    flights_list = add_flight_ui(flights_list)
                    print("Flight added successfully.")
                except ValueError as ve:
                    print(ve)
            elif choice == 2:
                try:
                    flights_list = delete_flight_ui(flights_list)
                    print("Flight deleted successfully.")
                except ValueError as ve:
                    print(ve)
            elif choice == 3:
                try:
                    result = departure_city_ui(flights_list)
                    sort_by_destination(result)
                    print("Here are the flight details for the given city: ")
                    display_list(result)
                except ValueError as ve:
                    print(ve)
            elif choice == 4:
                try:
                    flights_list = increase_duration_ui(flights_list)
                    print("The duration of the flights have been changed successfully.")
                except ValueError as ve:
                    print(ve)
            elif choice == 5:
                try:
                    print("Here are the flight details: ")
                    display_list(flights_list)
                except ValueError as ve:
                    print(ve)
        except ValueError as ve:
            print(ve)
if __name__ == '__main__':
    start()