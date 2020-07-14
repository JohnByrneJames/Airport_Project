from flight_algorithms import FlightBackEnd
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

    def __init__(self):
        # Class FlightFrontEnd
        pass

    @staticmethod
    def _verifying_employee():
        print("Welcome, please confirm your details.")

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
        # Later ( Assign staff to flight )

        # If no exceptions are raised -- create flight
        # Query database to create a flight with necessary information, make this available to customers who are booking
        # Send information to BackEnd to store in database
        pass

