from datetime import *
from Terminal.passengerinput import Passengers

class Add_person():
    selected_country = None

    def __init__(self, cursor):
        # Creating cursor class object
        self.cursor = cursor
        # Defining variables for later
        self.ticket_price = 3.00
        self.total_revenue = 2.00

    def flight_choice_country(self):
        # List countries
        sql_query = "SELECT DISTINCT Destination FROM Flights"
        rows = self.cursor.execute(sql_query)
        # Empty list to append to
        countries = []
        # Repeating for loop to append
        for row in rows:
            countries.append(row.Destination)
        print("\n" + str(countries))
        bool = True
        while bool == True:
            # User input to select country
            self.selected_country = input("\nSelect a country from the above list, and enter below. "
                                          "Please keep the same formatting.\n")
            try:
                if self.selected_country not in countries:
                    raise ValueError
            except ValueError:
                print("That is an invalid selection")
            else:
                bool = False

    def flight_choice_departure(self):
        # Calling previous function
        self.flight_choice_country()
        # List countries
        sql_query = ("SELECT DISTINCT DepartureDate FROM Flights WHERE Destination = '"+ self.selected_country+ "'")
        rows = self.cursor.execute(sql_query)
        # Empty list to append to
        dates = []
        # Repeating for loop to append
        for row in rows:
            x = row.DepartureDate
            dates.append(x.strftime("%Y/%m/%d"))
        print("\n" + str(dates))
        bool = True
        while bool == True:
            # User input to select departure date
            self.selected_departure_date = input("\nSelect a departure date from the above list, and enter below. "
                                                 "Please keep the same formatting.")
            try:
                if str(self.selected_departure_date) not in dates:
                    raise ValueError
            except ValueError:
                print("That is an invalid selection")
            else:
                bool = False


    def check_flight_capacity(self):
        # Get capacity of flight
        sql_query = "Select * FROM Flights WHERE DepartureDate = ? and Destination = ?"
        # Executing query using placeholder and wildcards
        rows = self.cursor.execute(sql_query, self.selected_departure_date, self.selected_country)
        # Printing out rows and creating variables from data fetched from table
        for row in rows:
            self.FlightID = row.FlightID
            self.flight_capacity = row.PassengerLimit
        print("The flight capacity for  flight {} is:".format(self.FlightID), self.flight_capacity)

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
        print("The current passenger count is:", self.current_passenger_count)

    def capacity_availability(self):
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
        self.buying_tickets = int(input("\nHow many people are you buying tickets for?\n"))
        # Making sure that not too many tickets are sold
        # Limit to 5 for looping reasons?
        if self.buying_tickets > int(self.spaces_remaining):
            print("\nThere is only {} spaces left, so {} tickets cannot be purchased.".format(self.spaces_remaining,self.buying_tickets))
        else:
            print("\nThere is enough spaces")
        # Input data into booking details page,using while loop to allow multiple record entry
        while True:
            user_input = input("\nWould you like to add booking details. Y or N\n")
            if user_input.upper() == "Y":
                # Creating class object for class of input methods
                obj1 = Passengers(self.cursor)
                # Calling input methods to insert customer data
                obj1.customer_input()
                obj1.choice_input(self.selected_country, self.FlightID)
            elif user_input.upper() == "N":
                print("\nThank you for your input, have a great day!")
                break
            # Print message confirming person added in
            print("\nDetails have been inserted into the database!")
            self.ticket_sale()

    def ticket_sale(self):
        # Calculating revenue
        # revenue = self.buying_tickets * self.ticket_price
        # # Adding revenue to total revenue and printing it
        # self.total_revenue += revenue
        print("\nTotal revenue so far is £", round(float(self.total_revenue), 3))
