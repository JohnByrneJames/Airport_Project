# As an airport assistant I want to be able to change flight trip details.
# If someone wanted to extend their departure date etc. Use a password.
import hashlib


class Change_details():
    # Predefining attributes
    current_departure_date = None
    destination = None
    current_flight = None
    new_departure_time = None
    new_departure_date = None
    flightid = None
    current_booking = None

    # Initialising class
    def __init__(self, cursor):
        # Creating cursor class object
        self.cursor = cursor
        self.current_booking = input("\nWhat TicketID would you like to work with?")

    # Method connecting booking details to flights
    def fetch_current_flight_details(self):
        # Use preset variable with person from list
        # Fetching current flight details of customer based on Ticket ID
        sql_query = (
            'SELECT * FROM BookingDetails BD INNER JOIN Flights F ON BD.FlightID = F.FlightID WHERE BD.TicketID = ?')
        # Executing query and printing result
        rows = self.cursor.execute(sql_query, self.current_booking)
        try:
            if rows.rowcount == 0:
                raise ValueError
        except ValueError:
            print("That ticketID has no flights associated with it")
        except:
            print("Error")
        else:
            for row in rows:
                print("The current departure date is:", row.DepartureDate, "\nThe destination is:", row.Destination)
                self.current_departure_date = row.DepartureDate
                self.destination = row.Destination
                self.current_flight = row.FlightID

    # Method to get possible flight option for date
    def show_flight_options_date(self):
        self.fetch_current_flight_details()
        # SQl query using current booking and desination to filter results
        sql_query = (
            "SELECT DISTINCT DepartureDate FROM BookingDetails BD LEFT JOIN Flights F ON BD.FlightID = F.FlightID "
            "WHERE F.Destination = ? and F.FlightID != ?")
        # Executing query and printing result
        rows = self.cursor.execute(sql_query, self.destination, self.current_flight)
        # Printing flights available or letting user know of availability
        if rows.rowcount == 0:
            print("\nNo alternative flights sorry")
            # Using return to end function
            return 0
        else:
            print("\nWhich departure date would you like to change to?")
            for row in rows:
                print("\nPossible departure date of:", row.DepartureDate)
            self.new_departure_date = input("\nEnter the new departure date here. Use yyyy/mm/dd formatting : ")

    # Method to get possible flight option for date
    def show_flight_options_time(self):
        self.show_flight_options_date()
        # SQl query using current booking and destination to filter results
        sql_query = (
            "SELECT Distinct DepartureTime FROM BookingDetails BD LEFT JOIN Flights F ON BD.FlightID = F.FlightID "
            "WHERE F.Destination = ? and F.FlightID != ? and F.DepartureDate = ?")
        # Executing query and printing result
        rows = self.cursor.execute(sql_query, self.destination, self.current_flight, self.new_departure_date)
        # Printing flights available or letting user know of availability
        if rows.rowcount == 0:
            print("\nNo alternative flights sorry")
            # Using return to end function
            return 0
        else:
            print("\nWhich departure time would you like to change to?")
            for row in rows:
                print("\nPossible departure time of:", row.DepartureTime)
            self.new_departure_time = input("\nEnter the new departure time here. Use hh/mm/ss formatting : ")

    # Get flight ID to change, for where departure date is x
    def fetch_flightID(self):
        self.show_flight_options_time()
        # Setting query
        sql_query = "SELECT FlightID FROM Flights WHERE DepartureDate = ? And DepartureTime = ?"
        # Executing query
        rows = self.cursor.execute(sql_query, self.new_departure_date, self.new_departure_time)
        for row in rows:
            self.flightid = row[0]

    # Updating booking details table to change flight ID to one with departure date
    def change_flight_details(self):
        # Calling previous method to get flight ID
        self.fetch_flightID()
        # Setting query
        sql_query = "UPDATE BookingDetails SET FlightID = ? WHERE TicketID = ?"
        # Executing query
        self.cursor.execute(sql_query, str(self.flightid), str(self.current_booking))
        # Committing change to SQL
        self.cursor.commit()
        # Print confirmation statement of flight details changing
        print("The flight has been changed. The FlightID is now:", self.flightid)