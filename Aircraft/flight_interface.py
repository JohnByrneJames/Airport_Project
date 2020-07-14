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
                if not self.__check_password(self.__username, self.__password):  # If true raise Error
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

        # If user has failed to login 3 times, then
        if user_login_attempts == 3:
            raise ValueError("\n⚠ 3 Login attempts have failed, exiting... ⚠")

    @staticmethod
    def _show_current_flights():
        # Welcome! Here are the current flights -->
        # Get flights from database and display them
        # What would you like to do?
        pass

    def _add_flight(self):
        # Create Flight
        # Ask for destination as well as departure date and time (refuse dates in the past or beyond a year in future)
        # Flight time (algorithm to work out times between departure time and landing time)

        # Set Passenger Limit (Not above models seat limit)

        # Later ( Assign staff to flight - List of available staff and assign them)

        # If no exceptions are raised -- create flight
        # Query database to create a flight with necessary information, make this available to customers who are booking
        # Send information to BackEnd to store in database
        pass
