#As an airport assistant I want to be able to change flight trip details.
#If someone wanted to extend their departure date etc. Use a password.

from connection import Connection

class Change_details(Connection):

    def __init__(self):
        pass

    def fetch_current_flight_details(self):
        # Sequel query connecting booking details to flights
        # Use preset variable with person from list
        booking_to_check = "1"
        sql_query = ("USE JMS_Airport\nDatabaseSELECT * FROM BookingDetails BD INNER JOIN Flights F ON BD.FlightID = F.FlightIDWHERE BD.TicketID =?", booking_to_check)
        self.cursor.execute(sql_query)
        return self.cursor

    def print_flight_details(self):
        rows = self.cursor.fetchone()
        for row in rows:
            print("Your current departure date is: ", row.DepatureDate)

    def change_flight_details(self):
        # Change flight ID to preset variable
        flight_change = "1"
        sql_query =


# Password function
# Prompt user to input password
# If equal to preset password then allow to change flight details

# Iteration 2
# Get user input for what person to change booking for
# Show flights to choose from
# Use user input to select whcih one
# Change flight associated with ticket in both tables