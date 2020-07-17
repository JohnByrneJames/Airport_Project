from Database_Connection.database_connection import DatabaseConnector
from datetime import datetime


# As an airport assistant, I want to create passengers with name AND passport number, so that I can add them to the flight. - Sohaib Sohail

class Passengers():
    # Precreating variables
    customer_firstname = None
    customer_surname = None
    customer_dateofbirth = None
    customer_passportnumber = None
    passportnum_input = None
    dateofbirth_input = None
    firstname_input = None
    surname_input = None
    destination_input = None

    # Intialising class and creating self.cursor object, as well as making sure correct database is in use
    def __init__(self, cursor):
        self.cursor = cursor
        # self.cursor.execute("use JMS_AirportDatabase")

    # Fetching data for customers and inserting it
    def customer_input(self):
        print("\nBefore we proceed to book the flight, we will need to take some details in order to process the "
              "transaction")
        # Getting names using input
        self.customer_firstname = input("\nPlease enter your first name: ").title()
        self.customer_surname = input("\nPlease enter your surname: ").title()
        # Defining bool value for while loop
        bool = True
        # While loop to check date of birth is in proper format, runs until format is correct
        while bool == True:
            self.customer_dateofbirth = input("\nPlease enter your date of birth. \nPlease enter the date in this "
                                              "[E.g. 2020-02-23] \n")
            # Try loop making sure format is correct
            try:
                # Raise value error if condition met
                if self.customer_dateofbirth != datetime.strptime(self.customer_dateofbirth, "%Y-%m-%d").strftime(
                        '%Y-%m-%d'):
                    raise ValueError
            # Defining what value error does
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                continue
            # Running code to stop while loop if try condition met
            else:
                # Boolean value is changed to false so while loop stops
                print("This is the correct date string format.")
                bool = False
        # Inserting customer data into table with wildcards to insert customer values
        sql_customer_query = ("INSERT INTO Customers(FirstName, LastName, DateOfBirth) VALUES(?, ?, ?)")
        # Executing and commiting query
        self.cursor.execute(sql_customer_query, self.customer_firstname, self.customer_surname,
                            self.customer_dateofbirth)
        self.cursor.commit()
        # Printing success message
        print(
            "Now that you've successfully entered into the JMS Airport system, let's proceed to the next step " + self.customer_firstname + " !")

    # Fetching customer ID with names and date of birth inputted previously
    def fetch_customerID(self):
        # Inserting customer data into table with wildcards to get customer values
        sql_query = "SElECT * FROM Customers WHERE FirstName = ? and LastName = ? and DateOfBirth = ?"
        # Executing query
        rows = self.cursor.execute(sql_query, self.customer_firstname, self.customer_surname, self.customer_dateofbirth)
        for row in rows:
            # Getting customerID of previously inserted customer
            self.customerID = row.CustomerID

    # Choice method allowing insertion of customer or booking details data
    def choice_input(self, destination, flightID):
        # Defining self values from values inserted when function called
        self.destination = destination
        self.flightID = flightID
        # While loop to make sure input is 1,2,3. else it will endlessly loop
        while True:
            self.user_choice = input("\nWelcome to the personalised Airport user experience. "
                                     "Please select one of the following options:""\n "
                                     "1. Do you want to book a flight for yourself? \n "
                                     "2. Do you want to book a flight for someone else? \n "
                                     "3. Exit\n")
            # Calling relevant methods depending on user choice
            if self.user_choice == 1:
                self.customer_booking_itself()
            elif self.user_choice == 2:
                self.customer_booking_someoneelse()
            elif self.user_choice == 3:
                break
            else:
                print("Unfortunately, you have selected the wrong output, please try again!")
                continue

    # Buying a ticket for yourself. Entering details as a customer before buying a ticket
    def customer_booking_itself(self):  # Ask user what they want, call the test function,
        print(
            "As you have already entered a few details, you only need to add your passport number. ")
        # Defining variables based on previously inserted ones
        self.destination_input = self.destination
        self.firstname_input = self.customer_firstname
        self.surname_input = self.customer_surname
        self.dateofbirth_input = self.customer_dateofbirth
        # Calling fetch customerID function to get customerID
        self.fetch_customerID()
        # Defining bool value for while loop
        bool = True
        # While loop with try loop to make sure passport is certain length
        while bool == True:
            self.passportnum_input = input("\nWhat is your passport number?\n")
            # Raise value error if condition met
            try:
                if len(self.passportnum_input) != 9:
                    raise ValueError
            # Defining what value error does
            except ValueError:
                print("Please enter the correct number")
                continue
            # If conditions met then while loop stops and success message printed
            else:
                print("Successfully accepted your passport number!")
                # Boolean value is changed to false so while loop stops
                bool = False
        # Inserting customer data into table with wildcards to insert customer values
        sql_self_customer_query = (
            "INSERT INTO BookingDetails(FlightID, CustomerID, FirstName, LastName, PassportNum, DateOfBirth) VALUES(?, ?, ?, ?, ?, ?)")
        # Executing query and commiting it to the database
        self.cursor.execute(sql_self_customer_query, self.flightID, self.customerID, self.customer_firstname,
                            self.customer_surname, self.passportnum_input, self.customer_dateofbirth)
        self.cursor.commit()
        # Printing success message
        print("You have successfully added a passenger to the flight list")

    # Buying it for someone else - customer details and passenger details
    def customer_booking_someoneelse(self):
        self.firstname_input = (input("\nWhat is the person's first name?\n").title())
        self.surname_input = (input("\nWhat is the person's surname?\n").title())
        self.fetch_customerID()

        # Defining bool value for while loop
        bool = True
        # While loop with try loop to make sure passport is certain length
        while bool == True:
            self.passportnum_input = (input("What is your passport number?\n"))
            # Raise value error if condition met
            try:
                if len(self.passportnum_input) != 9:
                    raise ValueError
            # Defining what value error does
            except ValueError:
                print("Please enter the correct number")
                continue
            # If conditions met then while loop stops and success message printed
            else:
                print("Successfully accepted your passport number!")
                # Boolean value is changed to false so while loop stops
                bool = False

        # Defining bool value for while loop
        bool = True
        # While loop with try loop to make sure date of birth is certain format
        while bool == True:
            self.dateofbirth_input = (
                input("\nWhat is the person's date of birth? Please enter the date in this format: YYYY-MM-DD"))
            # Try loop making sure format is correct
            try:
                # Raise value error if condition met
                if self.dateofbirth_input != datetime.strptime(self.dateofbirth_input, "%Y-%m-%d").strftime('%Y-%m-%d'):
                    raise ValueError
            # Defining what value error does
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
                continue
            # Running code to stop while loop if try condition met
            else:
                # Boolean value is changed to false so while loop stops
                print("This is the correct date string format.")
                bool = False

        # Inserting customer data into table with wildcards to insert customer values
        sql_passenger_query = (
            "INSERT INTO BookingDetails(FlightID, CustomerID, FirstName, LastName, PassportNum, DateOfBirth) VALUES(?, ?, ?, ?, ?, ?)")
        # Executing query and commiting it to the database
        self.cursor.execute(sql_passenger_query, self.flightID, self.customerID, self.firstname_input,
                            self.surname_input, self.passportnum_input, self.dateofbirth_input)
        self.cursor.commit()
        # Printing success message
        print("You have successfully added a passenger to the flight list")
