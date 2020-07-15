from new_connection import databaseconnection

from datetime import datetime
# As an airport assistant, I want to create passengers with name AND passport number, so that I can add them to the flight. - Sohaib Sohail

class Passengers():

    def __init__(self, cursor):
        self.firstname_input = (input(str(print("What is your first name?"))).title())
        self.surname_input = (input(str(print("What is your surname?"))).title())
        self.dateofbirth_input = (input(print("What is your date of birth? *Please enter the date in this format: YYYY-MM-DD*")))
        self.passportnumber_input = (input(print("What is your passport number?")))
        self.cursor = cursor

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

    def input_into_SQL(self):

        sql_query = ("INSERT INTO Customers(FirstName, LastName, DateOfBirth) VALUES(" + str(self.firstname_input) + str(self.surname_input) + str(self.dateofbirth_input) + ")")

        sql_query2 = ("INSERT INTO BookingDetails(PassportNum) VALUES(" + self.passportnumber_input + ")")

        self.cursor.execute(sql_query)
        self.cursor.execute(sql_query2)
        self.cursor.commit()

    def passenger_input_in_flights(self):

        sql_query3 = ("INSERT INTO BookingDetails(FirstName, LastName, PassportNum, DateOfBirth) VALUES(" + str(self.firstname_input) + str(self.surname_input) + (self.passportnumber_input) + self.dateofbirth_input + ")") #This is to insert data into the flights information

        self.cursor.execute(sql_query3)

        









    #
    # def validating_dateinput(d):
    #     try:
    #         if len(d) == 10:
    #             datetime.strptime(d, '%m/%d/%Y')
    #             return True
    #         else:
    #             return False
    #
    #     except ValueError:
    #         return False
    #
    #     print(validate_date('2/26/1000'))
    #

# databaseconnection()









