import pyodbc
import hashlib
import datetime as dt
import os

# This class works out the algorithmic details that are required in the interface class, therefore the complexity
# is hidden away from the user/ developer.
class FlightBackEnd:
    password_retrieved = None
    password_given = None
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

            self.password_given = self.__pass_hashing(password)

            if username != self.retrieved_username:
                raise ValueError
            elif self.password_given != self.password_retrieved:
                raise ValueError  # Raise error that password is incorrect
        except ValueError:
            return False  # Password not a match so return False
        else:
            return True  # Password match so return True

    @staticmethod
    def __pass_hashing(password):
        encoded = password.encode("utf-8")
        hashed_pass = hashlib.sha256(encoded)
        hashed_pass = hashed_pass.hexdigest()
        return hashed_pass

    def _get_flights(self, cursor):
        # >>> Check if None in flights -> Return "There are no flights"
        sql_query = 'SELECT * FROM FLights'
        try:
            rows = cursor.execute(sql_query)
            dict_of_flights = {}
            counter = 1
            # Go to database and retrieve all existing flights along with:
            # destination, departure date and time, Flight time

            print("-" * 80)
            print(" " * 30, "Existing Flight")
            print("-" * 80)

            for row in rows:  # Populate a dictionary with the flight information for future reference
                dict_of_flights["flight " + str(counter)] = {"Destination": row.Destination,
                                                             "DepartureDate": row.DepartureDate,
                                                             "DepartureTime": row.DepartureTime,
                                                             "FlightDuration": row.FlightDuration,
                                                             "PassengerLimit": row.PassengerLimit}
                print("Flight " + str(counter) + ": Departs at " + str(row.DepartureTime.strftime('%I:%M %p')) +
                      " on " + str(row.DepartureDate.strftime('%d %B, %Y')) + " Heading for " + row.Destination +
                      " with a flight time of " + self.create_time_and_hour(row.FlightDuration) + ".")
                counter += 1

        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):  # Catch common errors faced in pyodbc
            print("connection has timed out, or the database was not available \nNo point in retrying... "
                  "Please review connection credentials")
            return False  # Return false as it failed
        except Exception:
            print("\nAn unexpected error has occurred, if this persists please contact the system administrator...")
            return False  # Return false as it failed
        else:
            return True  # If success return True

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

    def generate_attendees_list(self, flight, cursor):
        # Clear attributes in-case they are previously used
        flight_details = ""
        flight_passengers = ""
        flight_id = ""

        # Check if flight is in database by FlightID
        sql = "SELECT * FROM Flights WHERE FlightID LIKE ?"
        rows = cursor.execute(sql, flight)

        if rows.rowcount == 0:
            print("\nNo Such Flight exists, Please try again...")
            return False  # This returns false as the flight ID is invalid
        else:
            for row in rows:
                flight_id = (str(row.FlightID) + "-" + row.Destination[:3].upper() + "0" +
                                          str(row.DepartureDate.day))
                flight_details = (
                      (str(row.FlightID) + "-" + row.Destination[:3].upper() + "0" + str(row.DepartureDate.day)) +
                      " destined for " + row.Destination + " on " + str(row.DepartureDate.day) + " "
                      + str(row.DepartureDate.strftime('%B')) + " " + str(row.DepartureDate.year) + " at "
                      + str(row.DepartureTime.strftime('%I:%M %p')))
        # The user has successfully selected a database
        print("\n" + flight_details)
        print("\nSuccessfully loaded a flight! Adding to file...")

        # Get all passengers on Flight
        # Check if flight already has a list generated, if so overwrite
        # Else create new one (Flight ID, Destination [first 3 letters],0 + departureTime[hour])

        sql = "SELECT * FROM BookingDetails WHERE FlightID = ?"
        rows = cursor.execute(sql, flight)

        counter = 1

        if rows.rowcount == 0:
            print("No passengers on this flight yet.")
            return False   # This returns false as the flight ID is invalid
        else:
            for row in rows:
                flight_passengers += ("[" + str(counter) + "]: " + row.FirstName + " "
                                      + row.LastName + " | Passport Number : " + row.PassportNum + "\n")
                counter += 1

        try:
            # Finally check if text file for this flights passenger list already exists
            with open("Generated_Manifests/" + flight_id + ".txt", "w+") as file:
                file.write("Flight Manifest for Flight " + str(flight_id) + "\n\n" + flight_details + "\n\n" +
                           "Passengers on This Flight: \n\n" + flight_passengers + "\n\n" + "Added on " +
                           self.create_time_stamp(dt.datetime.now()))
        except Exception:  # Starting with Exception as deadline is looming and this creates file, with unusual error
            print("Unusual error occurred")

        print("Success writing to manifest " + flight_id + ".txt\n")
        return True  # Text file has been created successfully

    @staticmethod
    def create_time_and_hour(minutes):
        if(minutes % 60) == 0:
            return str(minutes // 60) + " Hours"
        else:
            return str(minutes // 60) + " Hours " + str(minutes % 60) + " Minutes"

    @staticmethod
    def create_time_stamp(date):
        # Get date
        # Get suffix of day
        if 4 <= date.day <= 20 or 24 <= date.day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][date.day % 10 - 1]

        # Construct and Return timestamp
        return str(date.strftime("%d" + suffix + " %B %Y, at %I:%M %p"))

    def __work_out_landing_time(self, departure_time, flight_duration):
        # work out landing time via (departure_time + flight_duration = landing_time)
        pass
