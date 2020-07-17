from flight_interface import FlightFrontEnd
from add_person import Add_person
from create_staff_user import CreateStaffUser
from UserInterface.panda_representation import panda_data

class Interfacer:
    cursor = None

    def __init__(self, cursor):
        self.cursor = cursor

    def choose_interface(self):
        chosen = True

        while chosen:
            user_input = input("\nWelcome! What would you like to do?"
                               "\nStaff Access Portal [S] "
                               "\nCustomer Booking System [C] "
                               "\nView all Current Flights [F]"
                               "\nExit [E] ?")

            if user_input.lower() == "c":
                self.go_to_customer_interface()
            elif user_input.lower() == "s":
                have_an_account = input("Do you have a Staff account? [Y] [N] ")
                if have_an_account.lower() == "y":
                    self.go_to_staff_interface()
                elif have_an_account.lower() == "n":
                    self.create_staff_user()
                else:
                    continue
            elif user_input.lower() == "f":
                self.display_flights_in_panda()
            elif user_input.lower() == "e":
                self.exit_interface()
            else:
                print("\nNot recognised")

    def go_to_staff_interface(self):
        user_login = FlightFrontEnd(self.cursor)  # Create users login instance, with previously made connection
        user_login.user_login()  # Attempt login

    def go_to_customer_interface(self):
        user_login = Add_person(self.cursor)  # Create users login instance, with previously made connection
        user_login.flight_choice_departure()
        user_login.check_flight_capacity()
        user_login.check_passenger_count()
        user_login.capacity_availability()
        user_login.add_person()

    def create_staff_user(self):
        creation_inst = CreateStaffUser(self.cursor)
        creation_inst.insert_user_details()

    @staticmethod
    def exit_interface():
        exit("\nThank you for using with JMS Airlines \nSee you next time!")

    def display_flights_in_panda(self):
        panda_inst = panda_data()
        panda_inst.sql_query_with_panda()




