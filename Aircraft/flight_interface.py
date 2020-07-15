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
                self.__username = input(str("\nUsername [e.g. ex2307] : "))

                # If special characters are entered raise exception error
                if not set(self.__username).difference(ascii_letters, digits):
                    raise ValueError("\n⚠ The username should only include letters and numbers,"
                                     " no special characters [%$#@] ⚠")
                # Input left blank / less than 5 or greater than 5 characters
                elif 0 < len(self.__username) < 3 or len(self.__username) > 5:
                    raise ValueError("\n⚠ The username are always between 3 and 5 characters ⚠")

                self.__password = input(str("\nPassword :"))
                # Perform check of username / password simultaneously
                # Will return False if incorrect username or password (remains anonymous as to what)
                if not self.__check_password(self.__cursor, self.__username, self.__password):  # If true raise Error
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
                self.__add_flight()

        # If user has failed to login 3 times, then
        if user_login_attempts == 3:
            exit("\n⚠ 3 Login attempts have failed, exiting... ⚠")

    @staticmethod
    def _show_current_flights():
        # Welcome! Here are the current flights -->
        # Get flights from database and display them
        # What would you like to do?
        pass

    def __add_flight(self):
        print("\nWelcome! What would you like to do")
        print("\nCreate a new flight [c]\nRecall Help dialog [h]\nExit at any time with [e]:")
        exit_code_entered = False  # Boolean that handles whether or not the user has exited the loop
        while not exit_code_entered:
            users_input = input("What would you like to do? ")

            # Ask for destination as well as departure date and time (refuse dates in the past or beyond a year in
            # future) Flight time (algorithm to work out times between departure time and landing time)
            if users_input.lower() == "c":
                print("\nCreating a new flight...")
                try:  # Create Flight
                    destination = input("Whats is this flights destination? : ")
                    departure_date = input("What is the departure date of this flight? [E.g. 2018-03-19] : ")
                    departure_time = input("What is the departure time of this flight? [E.g. 13:00:00] : ")
                    flight_duration = input("Whats the flight duration? [E.g. 60 = 1 hour] : ")
                    passenger_limit = input("What is the passenger_limit? [E.g. 300] : ")

                    # Carry out checks on information - raise ValueError if something invalid
                    if any(map(str.isdigit, destination)): # Returns True if destination contains numbers (not allowed)
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
                except ValueError as e:
                    print(e)
                else:
                    # Create a dictionary with information
                    flight_dict = {}

        # Set Passenger Limit (Not above models seat limit)
        # Later ( Assign staff to flight - List of available staff and assign them)
        # If no exceptions are raised -- create flight
        # Query database to create a flight with necessary information, make this available to customers who are booking
        # Send information to BackEnd to store in database
        pass
