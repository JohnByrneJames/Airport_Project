from Database_Connection.database_connection import DatabaseConnector
import pandas as pd

from datetime import datetime
# As an airport assistant, I want to create passengers with name AND passport number, so that I can add them to the flight. - Sohaib Sohail

class Passengers():
    customer_firstname = None
    customer_surname = None
    customer_dateofbirth = None
    customer_passportnumber = None
    passportnum_input = None
    dateofbirth_input = None
    firstname_input = None
    surname_input = None
    destination_input = None

    def __init__(self, cursor):
        self.cursor = cursor
        # self.cursor.execute("use JMS_AirportDatabase")

    def customer_input(self):

        print("Before we proceed to book the flight, we will need to take some details in order to process the transaction\n")

        self.customer_firstname = str(input("Please enter your first name: \n").title())
        self.customer_surname = str(input("Please enter your surname: \n").title())
        self.customer_dateofbirth = input("Please enter your date of birth. \n *Please enter the date in this format: YYYY-MM-DD* \n")

        # while True:
        #     try:
        #          datetime.strptime(self.customer_dateofbirth, '%Y-%m-%d')
        #     except ValueError:
        #         print("This is the incorrect date string format. It should be YYYY-MM-DD")
        #         continue
        #     else:
        #         print("This is the correct date string format.")
        #     break

        sql_customer_query = ("INSERT INTO Customers(FirstName, LastName, DateOfBirth) VALUES(?, ?, ?)")

        self.cursor.execute(sql_customer_query, self.customer_firstname, self.customer_surname, self.customer_dateofbirth)
        self.cursor.commit()

        print("Now that you've successfully entered into the JMS Airport system, let's proceed to the next step " + self.customer_firstname + " !")

    def choice_input(self):

        self.user_choice = int(input("Welcome to the personalised Airport user experience. Please select one of the following options:"
    "\n 1. Do you want to book a flight for yourself? \n 2. Do you want to book a flight for someone else? \n"))

        while True:
            if self.user_choice == 1:
                self.customer_booking_itself()

            elif self.user_choice == 2:
                self.customer_booking_someoneelse()
            else:
                print("Unfortunately, you have selected the wrong output, please try again!")
                break


    def customer_booking_itself(self): #Ask user what they want, call the test function,

        print("As you have already entered a few details, you only need to add your passport number, and the choice of destination to proceed")

        # sql_query = ("SELECT * FROM Flights")
        # flights = self.cursor.execute(sql_query)
        # countries = []
        #
        # for flight in flights:
        #     destination = (flight.Destination)
        #     print("Your destination is" + destination)
        #     print(flight.DepartureDate)
        #     print(flight.)
        #     # print(flights)


        # self.destination_input = (input("What is your preferred destination? Please enter the same value in the table. \n"))

        self.firstname_input = self.customer_firstname
        self.surname_input = self.customer_surname

        while True:

            self.passportnum_input = (input("What is your passport number?\n"))

            try:
                if len(self.passportnum_input) != 9:
                    raise ValueError
            except ValueError:
                print("Please enter the correct number")
                continue
            else:
                print("Successfully accepted your passport number!")
                break

        self.dateofbirth_input = self.customer_dateofbirth

        sql_self_customer_query = ("INSERT INTO BookingDetails(FlightID, FirstName, LastName, PassportNum, DateOfBirth) VALUES(?, ?, ?, ?, ?)")

        self.cursor.execute(sql_self_customer_query, self.customer_firstname, self.customer_surname, self.passportnum_input, self.customer_dateofbirth)
        self.cursor.commit()

        print("You have successfully added a passenger to the flight list")


    def customer_booking_someoneelse(self):

        self.firstname_input = (input("What is the person's first name?\n").title())
        self.surname_input = (input("What is the person's surname?\n").title())


        while True:

            self.passportnum_input = (input("What is the person's passport number?\n"))

            try:
                if len(self.passportnum_input) != 9:
                    raise ValueError
            except ValueError:
                print("Please enter the correct number")
                continue
            else:
                print("Successfully accepted your passport number!")
                break

        self.dateofbirth_input = (input("What is the person's date of birth? *Please enter the date in this format: YYYY-MM-DD*\n"))

        while True:
            try:
                datetime.strptime(self.dateofbirth_input, '%Y-%m-%d')
                print("This is the correct date string format.")
            except ValueError:
                print("This is the incorrect date string format. It should be YYYY-MM-DD")
            break


        sql_passenger_query = ("INSERT INTO BookingDetails(FirstName, LastName, PassportNum, DateOfBirth) VALUES(?, ?, ?, ?)")

        self.cursor.execute(sql_passenger_query, self.firstname_input, self.surname_input, self.passportnum_input, self.dateofbirth_input)
        self.cursor.commit()

        print("You have successfully added a passenger to the flight list")


# #Buying a ticket for yourself. Entering details as a customer before buying a ticket
# #Buying it for someone else - customer details and passenger details
#
#
#









