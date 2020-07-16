from new_connection import databaseconnection

from datetime import datetime
# As an airport assistant, I want to create passengers with name AND passport number, so that I can add them to the flight. - Sohaib Sohail

class Passengers():

    def __init__(self, cursor):

        self.cursor = cursor

    def customer_input(self):

        print("Before we proceed to book the flight, we will need to take some details in order to process the transaction\n")

        self.customer_firstname = str(input("Please enter your first name").title())
        self.customer_surname = str(input("\nPlease enter your surname").title())
        self.customer_dateofbirth = input("\nPlease enter your date of birth. \n *Please enter the date in this format: YYYY-MM-DD*")

        self.dateofbirth_test()

        sql_customer_query = ("INSERT INTO Customers(FirstName, LastName, DateOfBirth) VALUES(" + str(self.customer_firstname) + str(self.customer_surname) + str(self.customer_dateofbirth) + ")")

        self.cursor.execute(sql_customer_query)
        self.cursor.commit()

        print("Now that you've successfully entered into the JMS Airport system, let's proceed to the next step " + self.customer_firstname + " !")

    def choice_input(self):

        self.user_choice = int(input("Welcome to the personalised Airport user experience. Please select one of the following options:"
    "\n 1. Do you want to book a flight for yourself? \n 2. Do you want to book a flight for someone else? \n 3. Change of mind? Do you want to edit a pre-booked flight? \n"))
        while True:
            if self.user_choice == 1:
                self.customer_booking_itself()

            elif self.user_choice == 2:
                self.customer_booking_someoneelse()

            elif self.user_choice == 3:


            else self.user_choice not in [1, 2, 3]:
                print("Unfortunately, you have selected the wrong output, please try again!")
            break

    def customer_booking_itself(self): #Ask user what they want, call the test function,

        print("As you have already entered a few details, you only need to add your passport number, and the choice of destination to proceed")

        self.firstname_input = self.customer_firstname
        self.surname_input = self.customer_surname
        self.passportnumber_input = (input("What is the person's passport number?"))
        self.dateofbirth_input = self.customer_dateofbirth

        self.passportnum_test()

        sql_query = ("INSERT INTO BookingDetails(FirstName, LastName, PassportNum, DateOfBirth) VALUES(" + self.firstname_input + self.surname_input + self.passportnumber_input + self.dateofbirth_input + ")")

        self.cursor.execute(sql_query)
        self.cursor.commit()

        print("You have successfully added a passenger to the flight list")

    def customer_booking_someoneelse(self):

        self.firstname_input = (input("What is the person's first name?").title())
        self.surname_input = (input("What is the person's surname?").title())
        self.passportnumber_input = (input("What is the person's passport number?"))
        self.dateofbirth_input = (input("What is the person's date of birth? *Please enter the date in this format: YYYY-MM-DD*"))

        self.dateofbirth_test()
        self.passportnum_test()

        sql_query = ("INSERT INTO BookingDetails(FirstName, LastName, PassportNum, DateOfBirth) VALUES(" + self.firstname_input + self.surname_input + self.passportnumber_input + self.dateofbirth_input + ")")

        self.cursor.execute(sql_query)
        self.cursor.commit()

        print("You have successfully added a passenger to the flight list")


    def dateofbirth_test(self):
        try:
            datetime.strptime(self.dateofbirth_input, '%Y-%m-%d')
            print("This is the correct date string format.")
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")


    def passportnum_test(self):
        try:
            if len(self.passportnumber_input) == 9 and type(self.passportnumber_input) == int:
                print("Successfully accepted your passport number")
        except ValueError:
            print("Please enter a number")
        else:
            print("Sorry, you have not entered the number correctly")


#
#     def passenger_input_in_flights(self):
#
#         sql_query3 = ("INSERT INTO BookingDetails(FirstName, LastName, PassportNum, DateOfBirth) VALUES(" + str(self.firstname_input) + str(self.surname_input) + (self.passportnumber_input) + self.dateofbirth_input + ")") #This is to insert data into the flights information
#
#         self.cursor.execute(sql_query3)
#         self.cursor.commit()
#
#
# #Buying a ticket for yourself. Entering details as a customer before buying a ticket
# #Buying it for someone else - customer details and passenger details
#
#
#









