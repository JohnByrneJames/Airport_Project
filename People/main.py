from change_details import Change_details
from add_person import Add_person
from Database_Connection.database_connection import DatabaseConnector
import os

# Defining database username etc variables
server = "databases.spartaglobal.academy"
database = "JMS_AirportDatabase"
username = os.environ.get('db_username')
password = os.environ.get('db_password')

database_link = DatabaseConnector(server, database, username, password)
connection = database_link.establish_connection()

# Calling functions
# Creating class instance
# obj1 = Change_details(connection)
# obj1.fetch_current_flight_details()
# obj1.show_flight_options_date()
# obj1.fetch_flightID()
# obj1.change_flight_details()
# obj1.insert_user_details()

# Calling functions
# Creating class instance
obj2 = Add_person(connection)
obj2.flight_choice_departure()
obj2.check_flight_capacity()
obj2.check_passenger_count()
# obj2.capacity_avaibility()
