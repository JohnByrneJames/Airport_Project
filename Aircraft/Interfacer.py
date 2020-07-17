from flight_interface import FlightFrontEnd
from People.add_person import Add_person

class Interfacer:
    cursor = None

    def __init__(self, cursor):
        self.cursor = cursor

    def choose_interface(self):
        chosen = True

        while chosen:
            user_input = input("\nWelcome! Are you a staff member [S] \nA customer [C]  \nor Exit [E] ?")

            if user_input.lower() == "c":
                self.go_to_customer_interface()
            elif user_input.lower() == "s":
                self.go_to_staff_interface()
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

    @staticmethod
    def exit_interface():
        exit("\nThanks for booking with JMS Airlines, see you next time")



