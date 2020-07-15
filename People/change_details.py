#As an airport assistant I want to be able to change flight trip details.
#If someone wanted to extend their departure date etc. Use a password.

from connection import Connection

class Change_details(Connection):

    def __init__(self, connection_string):
        # Inheriting connection string from parent class
        super().__init__(connection_string)
        # Use preset variable with person from list
        self.current_booking = input("What TicketID would you like to work with?")

    # Method connecting booking details to flights
    def fetch_current_flight_details(self):
        # Fetching current flight details of customer based on Ticket ID
        sql_query = ('SELECT * FROM BookingDetails BD INNER JOIN Flights F ON BD.FlightID = F.FlightID WHERE BD.TicketID =' + self.current_booking)
        # Excecuting query and printing result
        rows = self.cursor.execute(sql_query)
        for row in rows:
            print("Your current departure date is: ", row.DepartureDate, "\nYour destination is: ", row.Destination)
            self.current_departure_date = row.DepartureDate
            self.destination = row.Destination

    # Method to get possible flight options
    def show_flight_options(self):
        # SQl query using current booking and desination to filter results
        sql_query = ('SELECT * FROM BookingDetails BD LEFT JOIN Flights F ON BD.FlightID = F.FlightID WHERE F.Destination = \'' + self.destination + '\' and BD.TicketID != ' + self.current_booking)
        # Executing query and printing result
        rows = self.cursor.execute(sql_query)
        for row in rows:
            # Printing flights available or letting user no of availability
            if row[0] is None:
                print("No alternative flights sorry")
            else:
                print("Which departure date would you like to change to?")
                print("Possible departure date of:", row.DepartureDate)

    # Get flight ID to change, for where departure date is x
    def fetch_flightID(self):
        # Preset departure date
        new_departure_date = input("Enter the new departure date here. Use yyyy/mm/dd formatting.")
        departure_date = "'" + new_departure_date + "'"
        # Setting query
        sql_query = ("SELECT FlightID FROM Flights WHERE DepartureDate = "+ departure_date)
        # Executing query
        rows = self.cursor.execute(sql_query)
        for row in rows:
            self.flightid = row[0]
        print(self.flightid)

    # Updating booking details table to change flight ID to one with departure date
    def change_flight_details(self):
        # Calling previous method to get flight ID
        self.fetch_flightID()
        # Setting query
        sql_query = ("UPDATE BookingDetails SET FlightID =" + ("'" + str(self.flightid) + "'")) + "WHERE TicketID =" + ("'" + str(self.current_booking) + "'")
        # Executing query
        self.cursor.execute(sql_query)
        # Commiting change to SQL
        self.cursor.commit()
        # Print confirmation statement of flight details changing
        print("Your flight has been changed. Your FlightID is now:", self.flightid)


    def user_creation(self):
        # Take details on staff name

        # Use intials to create user name

        # Get user input for password

        # Check password is certain length
        pass


# Iteration 2
# Get user input for what person to change booking for Done
# Show flights to choose from Done
# Use user input to select which one Done
# Use country as well as departure date Done