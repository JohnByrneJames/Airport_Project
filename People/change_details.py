#As an airport assistant I want to be able to change flight trip details.
#If someone wanted to extend their departure date etc. Use a password.

from connection import Connection

class Change_details(Connection):

    def __init__(self, connection_string):
        super().__init__(connection_string)
        # Use preset variable with person from list
        self.current_booking = "7"

    def fetch_current_flight_details(self):
        # Sequel query connecting booking details to flights
        # Fetching current flight details of customer based on Ticket ID
        sql_query = ("SELECT * FROM BookingDetails BD INNER JOIN Flights F ON BD.FlightID = F.FlightID WHERE BD.TicketID =" + self.current_booking)
        self.cursor.execute(sql_query)
        rows = self.cursor.fetchall()
        for row in rows:
            print("Your current departure date is: ", row.DepartureDate)

    def show_flight_options(self):
        # sql_query = "Select * FROM Flights"
        sql_query = ("SELECT * FROM BookingDetails BD RIGHT JOIN Flights F ON BD.FlightID = F.FlightID WHERE TicketID !=" + self.current_booking)
        self.cursor.execute(sql_query)
        i = 0
        rows = self.cursor.fetchall()
        for row in rows:
            i += 1
            print(i, ". ", "Departure date of:", row.DepartureDate)

    # Get flight ID to change, for where departure date is x
    def fetch_flightID(self):
        # Preset departure date
        departure_date = "'2019/09/21'"
        # Setting query
        sql_query = ("SELECT FlightID FROM Flights WHERE DepartureDate = "+ departure_date)
        # Executing query
        self.cursor.execute(sql_query)
        rows = self.cursor.fetchall()
        for row in rows:
            self.flightid = int(row)
        print(self.flightid)

    # Updating booking details table to change flight ID to one with departure date
    def change_flight_details(self):
        # Calling previous method to get flight ID
        self.fetch_flightID()
        # Setting query
        sql_query = ("UPDATE BookingDetails SET FlightID =" + self.flightid + "WHERE TicketID =" + self.current_booking)
        # Executing query
        self.cursor.execute(sql_query)
        # Print confirmation statement of flight details changing
        print("Your flight has been changed")


# Password function
# Prompt user to input password
# If equal to preset password then allow to change flight details

# Iteration 2
# Get user input for what person to change booking for
# Show flights to choose from
# Use user input to select whcih one
# Change flight associated with ticket in both tables
# Use country as well as departure date