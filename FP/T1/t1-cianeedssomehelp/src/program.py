def create_flight(code: str, duration: int, departure_city: str, destination: str):
    if type(code) != str or type(duration) != int or type(departure_city) != str or type(destination) != str:
        raise ValueError("The parameters are not valid types.")
    if code == "" or departure_city == "" or destination == "":
        raise ValueError("The parameters should not be empty.")
    return {"code": code,"duration": duration, "departure_city": departure_city, "destination": destination}

def get_code(flight):
    return flight["code"]
def get_duration(flight):
    return flight["duration"]
def get_departure_city(flight):
    return flight["departure_city"]
def get_destination(flight):
    return flight["destination"]

def set_code(flight, new_code):
    flight["code"] = new_code
def set_duration(flight, new_duration):
    flight["duration"] = new_duration
def set_departure_city(flight, new_departure_city):
    flight["departure_city"] = new_departure_city
def set_destination(flight, new_destination):
    flight["destination"] = new_destination

def to_string(flights):
    code = get_code(flights)
    duration = get_duration(flights)
    departure_city = get_departure_city(flights)
    destination = get_destination(flights)
    return f"Flight: Code: {code}, Duration {duration}, Departure City: {departure_city}, Destination: {destination}"

def sort_by_destination(flights):
    for i in range(0, (len(flights)-1)):
        for j in range(i+1, len(flights)):
            if flights[j]["destination"] < flights[i]["destination"]:
                flights[j], flights[i] = flights[i], flights[j]
    return flights