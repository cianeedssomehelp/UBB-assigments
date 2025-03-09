from program import *

#
# Functionality 1
#

def add_flight(flights, code, duration, departure_city, destination):
    if type(code) != str or type(duration) != int or type(departure_city) != str or type(destination) != str:
        raise ValueError("The parameters are not valid types.")
    if len(code) < 3 or len(departure_city) < 3 or len(destination) < 3:
        raise ValueError("The parameters should not be less than 3 characters.")
    if duration < 20:
        raise ValueError("The duration must be greater or equal to 20 minutes.")
    for flight in flights:
        if get_code(flight) == code:
            raise ValueError("Each flight should have an unique code.")
    flight = create_flight(code, duration, departure_city, destination)
    flights.append(flight)
    return flights

#
# Functionality 2
# This function deletes a flight after the user inputs a flight code. If the flight with the given code does not exist then an Error is raised.
#

def delete_flight(flights, code):
    """
        Deletes a flight from the list with a given code.
       :param flights: our initial list of flights
       :param code: the code of the flight we are going to delete
       :return: the new list without the flight we deleted
       """
    found = False
    result = []
    for i in range(len(flights)):
        if get_code(flights[i]) != code:
            result.append(flights[i])
        else:
            found = True
    if found == False:
        raise ValueError("The flight code was not found.")
    flights.clear()
    flights.extend(result)
    return flights

#
# Functionality 3
#

def departure_city(flights, departure_city):
    found = False
    result = []
    for i in range(len(flights)):
        if get_departure_city(flights[i]) == departure_city:
            found = True
            result.append(flights[i])
    if not found:
        raise ValueError("The departure city doesn't exist.")
    return result

#
# Functionality 4
#

def increase_flight_duration(flights, departure_city, new_duration):
    found = False
    for i in range(len(flights)):
        if get_departure_city(flights[i]) == departure_city:
            set_duration(flights[i], new_duration)
            found = True
    if not found:
        raise ValueError("The departure city doesn't exist.")
    return flights


