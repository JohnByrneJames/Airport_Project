from connection import Connection

from datetime import *

# Inheriting the connection class to enable connection

class Add_person(Connection):

    def __init__(self, connection_string):
        # Inheriting connection string from parent class
        super().__init__(connection_string)
        # Defining variables for later
        self.ticket_price = 3.00
        self.total_revenue = 0.00

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
        # Executing query using placeholder and wildcards
        rows = self.cursor.execute(sql_query, self.selected_departure_date, self.selected_country)
        # Printing out rows and creating variables from data fetched from table
        for row in rows:
            self.FlightID = row.FlightID
            self.flight_capacity = row.PassengerLimit
        print(self.flight_capacity)

    def check_passenger_count(self):
        # Get amount of passengers per plane
        sql_query = "Select COUNT(*) FROM BookingDetails WHERE FlightID = ? "
        # Using wildcards (?s) to fill in placeholders with variables specified in execute command
        self.cursor.execute(sql_query, self.FlightID)
        # Fetching all rows then printing to get count of passengers per plane
        rows = self.cursor.fetchall()
        for row in rows:
            self.current_passenger_count = row[0]
        # Command for testing - delete later
        print(self.current_passenger_count)

    def capacity_avaibility(self):
        # Calculating and creating spaces remaining variable
        self.spaces_remaining = int(self.flight_capacity) - int(self.current_passenger_count)
        # Making sure that full planes are not available to book on
        if self.spaces_remaining < 0:
            print("There is no more availability on this flight.")
        else:
            print("There is {} spaces remaining".format(self.spaces_remaining))

    def add_person(self):
        # Age limiter - baby age means no seat
        # Find out how many tickets are being bought
        self.buying_tickets = int(input("How many people are you buying tickets for?\n"))
        # Making sure that not too many tickets are sold
        if self.buying_tickets > self.spaces_remaining:
            pass
        else:
            print("There is only {} spaces left, so {} tickets cannot be purchased.". format(self.spaces_remaining, self.buying_tickets))
        # Input data into booking details page,using while loop to allow multiple record entry
        while True:
            user_input = ("Would you like to add more booking details. Y or N")
            if user_input.upper() == "Y":
                # Call sohaib user story to insert customer details
                # sql_query = ("")
                # self.cursor.execute(sql_query, )
                # self.cursor.commit()
                pass
            elif user_input.upper() == "N":
                break
        # Print message confirming person added in
        print("Details for {} have been inserted into the database!")

    def ticket_sale(self):
        # Calculating revenue
        revenue = self.buying_tickets * self.ticket_price
        # Adding revenue to total revenue and printing it
        self.total_revenue += revenue
        print("Total revenue so far is £", self.total_revenue)

        self.ticket_price = 3.00

    def flight_choice(self):
        pass
        # List countries
        # User input to select country

    def check_capacity(self):
        pass

    def add_person(self):
        pass

    def ticket_sale(self):
        pass

