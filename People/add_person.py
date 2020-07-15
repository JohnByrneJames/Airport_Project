from connection import Connection
from datetime import *

class Add_person(Connection):

    def __init__(self, connection_string):
        # Inheriting connection string from parent class
        super().__init__(connection_string)
        self.ticket_price = 3.00

    def flight_choice_country(self):
        # List countries
        sql_query = "SELECT * FROM Flights"
        rows = self.cursor.execute(sql_query)
        # Empty list to append to
        countries = []
        # Repeating for loop to append
        for row in rows:
            countries.append(row.Destination)
        print(countries)
        # User input to select country
        self.selected_country = input("Select a country from the above list, and enter below. Please keep the same formatting.\n ")

    def flight_choice_departure(self):
        # Calling previous function
        self.flight_choice_country()
        # List countries
        sql_query = ("SELECT * FROM Flights WHERE Destination = '"+ self.selected_country+ "'")
        rows = self.cursor.execute(sql_query)
        # Empty list to append to
        dates = []
        # Repeating for loop to append
        for row in rows:
            x = row.DepartureDate
            dates.append(x.strftime("%Y/%m/%d"))
        print(dates)
        # User input to select country
        self.selected_departure_date = input("Select a departure date from the above list, and enter below. Please keep the same formatting.\n ")

    def check_flight_capacity(self):
        # Get capacity of flight
        sql_query = "Select * FROM Flights WHERE DepartureDate = ? and Destination = ?"
        rows = self.cursor.execute(sql_query, self.selected_departure_date, self.selected_country)
        for row in rows:
            self.FlightID = row.FlightID
            self.flight_capacity = row.PassengerLimit
        print(self.flight_capacity)

    def check_passenger_count(self):
        # Get amount of passengers per plane
        sql_query = "Select COUNT(*) FROM BookingDetails WHERE FlightID = ? "
        self.cursor.execute(sql_query, self.FlightID)
        rows = self.cursor.fetchall()
        for row in rows:
            self.current_passenger_count = row[0]
        print(self.current_passenger_count)

    def capacity_avaibility(self):
        self.spaces_remaining = int(self.flight_capacity) - int(self.current_passenger_count)
        if self.spaces_remaining < 0:
            print("There is no more availability on this flight.")
        else:
            print("There is {} spaces remaining".format(self.spaces_remaining))

    def add_person(self):
        # Age limiter - baby age means no seat
        buying_tickets = int(input("How many people are you buying tickets for?\n"))
        if buying_tickets > self.spaces_remaining:

        # Input data into booking details page

        # Print message confirming person added in
        pass

    def ticket_sale(self):
        pass
