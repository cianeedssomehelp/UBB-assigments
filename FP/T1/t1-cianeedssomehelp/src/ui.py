from services import *

def printMenu():
    print("Here's what you can do:")
    print("1. Add a flight.")
    print("2. Delete a given flight.")
    print("3. View all flights with a given departure city.")
    print("4. Increase duration of flight.")
    print("5. Show all flights.")
    print("0. Exit the application.")

def display_list(flights):
    for i in range (len(flights)):
        if isinstance(flights[i], dict):
            print(to_string(flights[i]))
        else:
            raise ValueError("The flight you entered is not a dictionary.")

def add_flight_ui(flights):
    try:
        code = input("Enter the flight code: ")
        duration = int(input("Enter the flight duration: "))
        departure_city = input("Enter the departure city: ")
        destination = input("Enter the destination city: ")
    except ValueError as ve:
        raise ValueError(ve)
    flights = add_flight(flights, code, duration, departure_city, destination)
    return flights

def delete_flight_ui(flights):
    try:
        code = input("Enter the flight code: ")
        if type(code) != str:
            raise ValueError("Invalid input.")
    except ValueError as ve:
        raise ValueError(ve)
    flights = delete_flight(flights, code)
    return flights

def departure_city_ui(flights):
    try:
        departure = input("Enter the flight departure city: ")
        if type(departure) != str:
            raise ValueError("Invalid input.")
    except ValueError as ve:
        raise ValueError("ve")
    result = departure_city(flights, departure)
    return result

def increase_duration_ui(flights):
    try:
        departure = input("Enter the flight departure city: ")
        if type(departure) != str:
            raise ValueError("Invalid input.")
        new_duration = int(input("Enter the new duration: "))
        if new_duration < 10 or new_duration > 60:
            raise ValueError("Invalid duration. Please enter a number between 10 and 60.")
    except ValueError as ve:
        raise ValueError(ve)
    flights = increase_flight_duration(flights, departure, new_duration)
    return flights