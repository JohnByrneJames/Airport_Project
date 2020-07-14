# This class works out the algorithmic details that are required in the interface class, therefore the complexity
# is hidden away from the user/ developer.
class FlightFrontEnd:
    def __init__(self):
        # Class FlightFrontEnd
        pass

    def __check_password(self, password):
        # Compare password against stored password (hash?)
        pass

    def __get_flights(self):
        # >>> Check if None in flights -> Return "There are no flights"
        # Go to database and retrieve all existing flights along with:
        # destination, departure date and time, Flight time,
        pass

    def __create_new_flight(self, destination, departure_date, departure_time, flight_duration, passenger_limit):
        # If the checks have been successfully passed then create the flight in the database using parameters received
        # work out landing time via (departure_time + flight_duration = landing_time)
        pass

    def __work_out_landing_time(self, departure_time, flight_duration):
        # work out landing time via (departure_time + flight_duration = landing_time)
        pass



