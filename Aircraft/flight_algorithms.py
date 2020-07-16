import pyodbc

# This class works out the algorithmic details that are required in the interface class, therefore the complexity
# is hidden away from the user/ developer.
class FlightBackEnd:
    password_retrieved = None
    retrieved_username = None
    dictionary_of_new_flight = None

    def __init__(self):
        # Class FlightFrontEnd
        pass

    def check_password(self, cursor, username, password):
        try:
            sql_query = 'SELECT * FROM Staff WHERE Username LIKE ?'
            rows = cursor.execute(sql_query, username)
            for row in rows:
                self.password_retrieved = row.Password  # store password in extracted rows
                self.retrieved_username = row.Username

            if username != self.retrieved_username:
                raise ValueError
            elif password != self.password_retrieved:
                raise ValueError  # Raise error that password is incorrect
        except ValueError:
            return False  # Password not a match so return False
        else:
            return True  # Password match so return True

    def __get_flights(self, cursor):
        # >>> Check if None in flights -> Return "There are no flights"
        cursor
        # Go to database and retrieve all existing flights along with:
        # destination, departure date and time, Flight time,
        pass

    def create_new_flight(self, flight_dictionary, cursor):
        self.dictionary_of_new_flight = flight_dictionary

        # If the checks have been successfully passed then create the flight in the database using parameters received
        # work out landing time via (departure_time + flight_duration = landing_time)
        sql_query = ("INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit)"
                     "VALUES(?, ?, ?, ?, ?)")
        cursor.execute(sql_query,
                       self.dictionary_of_new_flight['Destination'],
                       self.dictionary_of_new_flight['Departure_date'],
                       self.dictionary_of_new_flight['Departure_time'],
                       self.dictionary_of_new_flight['Flight_duration'],
                       self.dictionary_of_new_flight['Passenger_limit'])
        cursor.commit()
        print("\nFlight successfully added")

    def __work_out_landing_time(self, departure_time, flight_duration):
        # work out landing time via (departure_time + flight_duration = landing_time)
        pass
