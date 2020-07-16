from flight_algorithms import FlightBackEnd
from string import ascii_letters, digits  # Check for special characters


# User story
# As an airport assistant, I want to create a flight trip with a specific destination. - John

# Flight class capable of creating a flight
# The flight needs to fit these criteria:
# - Destination
# - DepartureDate
# - DepartureTime
# - FlightDuration
# - PassengerLimit

# User Story
# As an airport assistant I want to be able to generate a flight_attendees_list that lists passenger names and passports
# to check identity.

# To do this, the booking_details table needs to return:
# - First Name
# - Last Name
# - Passport Number

# Perhaps date of birth later on
# - Date of Birth

class FlightFrontEnd(FlightBackEnd):
    __cursor = None
    # This will be used to verify the identity of the employee trying to log in
    __username = None
    __password = None

    def __init__(self, cursor):
        # Class FlightFrontEnd
        super().__init__()
        self.__cursor = cursor

    def user_login(self):
        user_login_attempts = 0  # Track attempts to login
        print("Welcome, please confirm your details.")
        while user_login_attempts <= 3:  # If user has failed to login 3 times escape.
            try:
                self.__username = input(str("\nUsername [e.g. ex230] : "))

                # If special characters are entered raise exception error
                if set(self.__username).difference(ascii_letters, digits):
                    raise ValueError("\n⚠ The username should only include letters and numbers,"
                                     " no special characters [%$#@] ⚠")
                # Input left blank / less than 5 or greater than 5 characters
                elif 0 < len(self.__username) < 3 or len(self.__username) > 5:
                    raise ValueError("\n⚠ The username are always between 3 and 5 characters ⚠")

                self.__password = input(str("\nPassword : "))
                # Perform check of username / password simultaneously
                # Will return False if incorrect username or password (remains anonymous as to what)
                if not self.check_password(self.__cursor, self.__username, self.__password):  # If true raise Error
                    raise ValueError("\n⚠ Password or Username is incorrect ⚠")
            except ValueError as e:
                print(e)
                user_login_attempts += 1  # Increase login attempts
                continue  # continue to next iteration, allow user to retry
            except Exception:  # Base exception class to catch any unexpected exceptions
                print("\nAn unexpected error has occurred, if this persists please contact the system administrator...")
                # This occurs only if a weird error occurs, to handle this the program will exit and they can retry
                exit("Exiting! Please retry from the main menu.")  # This exits with a message to the user
            else:  # The user has successfully logged in as no exceptions were raised
                print("Welcome! " + self.__username)
                self.__user_interface()

        # If user has failed to login 3 times, then
        if user_login_attempts == 3:
            exit("\n⚠ 3 Login attempts have failed, exiting... ⚠")

    def _show_current_flights(self):
        # Welcome! Here are the current flights -->
        # Get flights from database and display them
        # What would you like to do?
        return self._get_flights(self.__cursor)  # Load flights

    def __add_flight(self):
        try:  # Create Flight
            destination = input("Whats is this flights destination? : ")
            if self.check_if_exit(destination):  # Allows exiting of program at any time with 'e'
                return False
            departure_date = input("What is the departure date of this flight? [E.g. 2018-03-19] : ")
            if self.check_if_exit(destination):  # Allows exiting of program at any time with 'e'
                return False
            departure_time = input("What is the departure time of this flight? [E.g. 13:00:00] : ")
            if self.check_if_exit(destination):  # Allows exiting of program at any time with 'e'
                return False
            flight_duration = input("Whats the flight duration? [E.g. 60 = 1 hour] : ")
            if self.check_if_exit(destination):  # Allows exiting of program at any time with 'e'
                return False
            passenger_limit = input("What is the passenger_limit? [E.g. 300] : ")
            if self.check_if_exit(destination):  # Allows exiting of program at any time with 'e'
                return False

            # Carry out checks on information - raise ValueError if something invalid
            if any(map(str.isdigit, destination)):  # Returns True if destination contains numbers (not allowed)
                raise ValueError("\n⚠ A Destination cannot contain a number, please retry ⚠")
            elif len(departure_date) != 10:
                raise ValueError("\n⚠ Your date isn't in the format YYYY-MM-DD, please retry ⚠")
            elif len(departure_time) != 8:
                raise ValueError("\n⚠ Your date isn't in the format HH:MM:SS, please retry ⚠")
            elif not any(map(str.isdigit, flight_duration)):  # This contains a letter, should only be numbers
                raise ValueError("\n⚠ Your duration contains a letter, use the format 60 / "
                                 "1 hour, please retry ⚠")
            elif not any(map(str.isdigit, passenger_limit)):  # This contains a letter, should only be numbers
                raise ValueError("\n⚠ Your passenger limit contains letters, use numbers only, please retry ⚠")

            # Present the details that have been given by the employee.
            while True:
                final_check = input("\nIs this correct? [Y] or [N]\n"
                                    "Destination :" + destination + "\n"
                                    "Departure Date :" + departure_date + "\n"
                                    "Departure time :" + departure_time + "\n"
                                    "Flight Duration :" + flight_duration + "\n"
                                    "Passenger Limit :" + passenger_limit + "\n")

                if final_check.lower() == 'y':
                    print("\nAdding the flight to the list of existing flights...")
                    break  # break out internal loop
                if final_check.lower() == 'n':
                    print("\nOkay, Restarting...")
                    self.__add_flight()  # Restarts method
                else:
                    print("\nDid not recognise that response.")
                    continue  # Asks the questions again
        except ValueError as e:
            print(e)
            return False
        except Exception:
            print("Sorry! an unexpected error occurred, please try again.")
            return False
        else:
            # The input didn't hit any exception nets and is moving on now
            # Create a dictionary with information, make necessary conversions
            flight_dict = {"Destination": destination, "Departure_date": departure_date,
                           "Departure_time": departure_time, "Flight_duration": int(flight_duration),
                           "Passenger_limit": int(passenger_limit)}
            # If no exceptions are raised -- create flight
            # Send information to BackEnd to store in database
            self.create_new_flight(flight_dict, self.__cursor)
            return True

    def __user_interface(self):
        print("\nWelcome! What would you like to do")
        help_message = "\nCreate a new flight [c]\nView all current flights [f]\nRecall Help dialog [h]" \
                       "\nExit at any time with [e]:"
        print(help_message)
        exit_code_entered = False  # Boolean that handles whether or not the user has exited the loop
        while not exit_code_entered:
            users_input = input("What would you like to do? ")

            # Ask for destination as well as departure date and time (refuse dates in the past or beyond a year in
            # future) Flight time (algorithm to work out times between departure time and landing time)
            if users_input.lower() == "c":
                print("\nCreating a new flight...")
                if self.__add_flight():  # Returns True if success and False if failure
                    print("\nSuccess!\n")
                else:
                    print("\nRestarting\n")
                    continue  # Restart interface
            elif users_input.lower() == "h":
                print(help_message)
            elif users_input.lower() == "f":
                print("\nLoading flights now..")
                if self._show_current_flights():  # If true is returned successfully loaded
                    print("\nSuccessfully loaded flight information")
                    continue
                else:  # Returns false the flight information couldn't be loaded
                    print("\nSorry! an error occurred, restarting interface...")
                    continue

            elif users_input.lower() == "e":
                print("\nExiting System...")
                exit_code_entered = True  # Change exit code to True as 'e' was entered, E.G (will break while loop)

        exit("\nSee you next time " + self.__username + "!")
        # To Do List:
        # Set Passenger Limit (Not above models seat limit)
        # Later ( Assign staff to flight - List of available staff and assign them)

    def __generate_flight_attendees_list(self):

        pass

    @staticmethod
    def check_if_exit(user_input):
        if user_input == 'e':
            return True
        else:
            return False
