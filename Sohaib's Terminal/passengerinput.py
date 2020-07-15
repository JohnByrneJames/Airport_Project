from new_connection import databaseconnection

from datetime import datetime
# As an airport assistant, I want to create passengers with name AND passport number, so that I can add them to the flight. - Sohaib Sohail

class Passengers():

    def __init__(self):
        self.firstname_input = None
        self.surname_input = None
        self.dateofbirth_input = None
        self.passportnumber_input = None

    def passenger_input(self):
        self.firstname_input = (input(str(print("What is your first name?"))).title())
        self.surname_input = (input(str(print("What is your surname?"))).title())
        self.dateofbirth_input = (input(print("What is your date of birth? *Please enter the date in this format: YYYY-MM-DD*")))

        try:
            datetime.strptime(self.dateofbirth_input, '%Y-%m-%d')
            print("This is the correct date string format.")
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")

        self.passportnumber_input = (input(print("What is your passport number?")))

        try:
            if len(self.passportnumber_input) == 9 and type(self.passportnumber_input) == int:
                print("Successfully accepted your passport number")
        except ValueError:
            print("Please enter a number")
        else:
            print("Sorry, you have not entered the number correctly")

        sql_query = ("INSERT INTO Customers(FirstName, LastName, DateOfBirth) VALUES(" + self.firstname_input + self.surname_input + self.dateofbirth_input + ")")

        self.cursor.execute(sql_query)









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









