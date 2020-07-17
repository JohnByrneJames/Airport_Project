# As an airport assistant I want to be able to change flight trip details.
# If someone wanted to extend their departure date etc. Use a password.
import hashlib


class Change_details():
    # Predefining attributes
    current_departure_date = None
    destination = None
    current_flight = None
    new_departure_time = None
    new_departure_date = None
    flightid = None
    staff_name = None
    staff_position = None
    staff_username = None
    staff_password = None
    staff_password_encrypted = None

    # Initialising class
    def __init__(self, cursor):
        # Creating cursor class object
        self.cursor = cursor
        # Use preset variable with person from list
        self.current_booking = input("What TicketID would you like to work with?")

    # Method connecting booking details to flights
    def fetch_current_flight_details(self):
        # Fetching current flight details of customer based on Ticket ID
        sql_query = ('SELECT * FROM BookingDetails BD INNER JOIN Flights F ON BD.FlightID = F.FlightID WHERE BD.TicketID = ?')
        # Executing query and printing result
        rows = self.cursor.execute(sql_query, self.current_booking)
        try:
            if rows.rowcount == 0:
                raise ValueError
        except ValueError:
            print("That ticketID has no flights associated with it")
        except:
            print("Error")
        else:
            for row in rows:
                print("The current departure date is:", row.DepartureDate, "\nThe destination is:", row.Destination)
                self.current_departure_date = row.DepartureDate
                self.destination = row.Destination
                self.current_flight = row.FlightID

    # Method to get possible flight option for date
    def show_flight_options_date(self):
        self.fetch_current_flight_details()
        # SQl query using current booking and desination to filter results
        sql_query = ("SELECT DISTINCT DepartureDate FROM BookingDetails BD LEFT JOIN Flights F ON BD.FlightID = F.FlightID WHERE F.Destination = ? and F.FlightID != ?")
        # Executing query and printing result
        rows = self.cursor.execute(sql_query, self.destination, self.current_flight)
        # Printing flights available or letting user know of availability
        if rows.rowcount == 0:
            print("No alternative flights sorry")
            # Using return to end function
            return 0
        else:
            print("Which departure date would you like to change to?")
            for row in rows:
                print("Possible departure date of:", row.DepartureDate)
            self.new_departure_date = input("Enter the new departure date here. Use yyyy/mm/dd formatting.")

     # Method to get possible flight option for date
    def show_flight_options_time(self):
         self.show_flight_options_date()
         # SQl query using current booking and destination to filter results
         sql_query = ("SELECT Distinct DepartureTime FROM BookingDetails BD LEFT JOIN Flights F ON BD.FlightID = F.FlightID WHERE F.Destination = ? and F.FlightID != ? and F.DepartureDate = ?")
         # Executing query and printing result
         rows = self.cursor.execute(sql_query, self.destination, self.current_flight, self.new_departure_date)
         # Printing flights available or letting user know of availability
         if rows.rowcount == 0:
             print("No alternative flights sorry")
             # Using return to end function
             return 0
         else:
            print("Which departure time would you like to change to?")
            for row in rows:
                print("Possible departure time of:", row.DepartureTime)
            self.new_departure_time = input("Enter the new departure time here. Use hh/mm/ss formatting.")

    # Get flight ID to change, for where departure date is x
    def fetch_flightID(self):
        self.show_flight_options_time()
        departure_date = "'" + self.new_departure_date + "'"
        # Setting query
        sql_query = ("SELECT FlightID FROM Flights WHERE DepartureDate = " + departure_date)
        # Executing query
        rows = self.cursor.execute(sql_query)
        for row in rows:
            self.flightid = row[0]
        print(self.flightid)

    # Updating booking details table to change flight ID to one with departure date
    def change_flight_details(self):
        # Calling previous method to get flight ID
        self.fetch_flightID()
        # Setting query
        sql_query = ("UPDATE BookingDetails SET FlightID = ? WHERE TicketID = ?")
        # Executing query
        self.cursor.execute(sql_query, str(self.flightid), str(self.current_booking))
        # Commiting change to SQL
        self.cursor.commit()
        # Print confirmation statement of flight details changing
        print("The flight has been changed. Your FlightID is now:", self.flightid)

    def user_creation(self):
        # Take details on staff name
        self.staff_name = input("What is your name?\n")
        self.staff_position = input("What is your position?\n")
        # Using initials to create user name
        self.staff_username = (self.staff_name[0:3]).upper() + (self.staff_position[0])
        self.password_creator()

    def password_creator(self):
        # Get user input for password
        print("A password should be at least 7 characters long\n")
        # Check password is certain length, using try except loop
        try:
            self.staff_password = input("Enter you password here\n")
            if len(self.staff_password) > 7:
                pass
            else:
                raise Exception("incorrect")
        except "incorrect":
            print("Your password is not long enough, make sure it is 7 characters")
        except:
            print("Error")
        # Using if loop to check password is same when retyped.
        staff_password_check = input("Enter your password again\n")
        # If loop to verify password using double entry
        if staff_password_check == self.staff_password:
            print("Your password has been set, make sure to remember it")
        else:
            print("That was not correct, please recreate your password")
            self.password_creator()
        self.encrypt_password()

    def encrypt_password(self):
        # Encoding intial variable
        self.staff_password = self.staff_password.encode('utf-8')
        # Hashing password
        hash_object = hashlib.sha256(self.staff_password)
        self.staff_password_encrypted = hash_object.hexdigest()

    def insert_user_details(self):
        # Calling previous method to ensure user details are created
        self.user_creation()
        # Creating SQL query with wild cards to be placeholders
        sql_query = "INSERT INTO Staff(Name, [Position], Username, password)VALUES (?, ?, ?, ?)"
        # Executing query with variables put in.
        self.cursor.execute(sql_query, self.staff_name, self.staff_position, self.staff_username,
                            str(self.staff_password_encrypted))
        # Commiting query to make sure data has been inputted
        self.cursor.commit()
        # Printing success message
        print("Your user details have successfully been inputted")
