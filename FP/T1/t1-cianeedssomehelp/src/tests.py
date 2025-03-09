from services import *

#
# Test for the functionality that deletes a flight after the user inputs one of the flight codes.
#

def test_delete_flight():
    flights = [
        {"code": "100A", "duration": 30, "departure_city": "Barcelona", "destination": "Cluj-Napoca"},
        {"code": "101B", "duration": 40, "departure_city": "Bucuresti", "destination": "Rome"},
        {"code": "103C", "duration": 50, "departure_city": "London", "destination": "Paris"}
    ]
    delete_flight(flights, "101B")
    assert flights == [{"code": "100A", "duration": 30, "departure_city": "Barcelona", "destination": "Cluj-Napoca"},
                       {"code": "103C", "duration": 50, "departure_city": "London", "destination": "Paris"}
                       ], "test_delete_flight failed"

def run_tests():
    try:
        test_delete_flight()
        print("Test passed")
    except AssertionError as ae:
        print(ae)
run_tests()
