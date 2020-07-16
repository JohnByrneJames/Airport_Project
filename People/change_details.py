#As an airport assistant I want to be able to change flight trip details.
#If someone wanted to extend their departure date etc. Use a password.
import hashlib

from connection import Connection

class Change_details(Connection):

    # Initialising class
    def __init__(self, connection_string):
        # Inherting connection string from parent class
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
            print("The current departure date is: ", row.DepartureDate, "\nThe destination is: ", row.Destination)
            self.current_departure_date = row.DepartureDate
            self.destination = row.Destination
            self.current_flight = row.FlightID

    # Method to get possible flight options
    def show_flight_options(self):
        # SQl query using current booking and desination to filter results
        sql_query = ('SELECT DISTINCT DepartureDate FROM BookingDetails BD LEFT JOIN Flights F ON BD.FlightID = F.FlightID WHERE F.Destination = \'' + self.destination + '\' and F.FlightID != ' + str(self.current_flight))
        # Executing query and printing result
        rows = self.cursor.execute(sql_query)
        # Printing flights available or letting user know of availability
        if rows.rowcount == 0:
            print("No alternative flights sorry")
            # Using return to end function
            return 0
        else:
            print("Which departure date would you like to change to?")
            for row in rows:
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
        self.staff_name = input("What is your full name?\n")
        self.staff_position = input("What is your position?\n")
        # Using initials to create user name
        self.staff_username = (self.staff_name[0:4]) + (self.staff_position[0])
        self.password_creator()

    def password_creator(self):
        # Get user input for password
        print("A password should be at least 7 characters long\n")
        # Check password is certain length, using try except loop
        try:
            self.staff_password = input("Enter you password here\n")
            if len(self.staff_password) > 7:
                pass
            else:
                raise Exception("incorrect")
        except "incorrect":
            print("Your password is not long enough, make sure it is 7 characters")
        except:
            print("Error")
        # Using if loop to check password is same when retyped.
        staff_password_check = input("Enter your password again\n")
        if staff_password_check == self.staff_password:
            print("Your password has been set, make sure to remember it")
        else:
            print("That was not correct, please recreate your password")
            self.password_creator()

    def insert_user_details(self):


# Iteration 2
# Get user input for what person to change booking for Done
# Show flights to choose from Done
# Use user input to select which one Done
# Use country as well as departure date Done