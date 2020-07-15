from change_details import Change_details
from add_person import Add_person
import os

# Defining database username etc variables
server = "databases.spartaglobal.academy"
database = "JMS_AirportDatabase"
username = os.environ.get('db_username')
password = os.environ.get('db_password')

# Creating connections string object with variables
connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


# Calling functions
# Creating class instance
# obj1 = Change_details(connection_string)
# obj1.use_database()
# obj1.fetch_current_flight_details()
# obj1.show_flight_options()
# # obj1.fetch_flightID()
# obj1.change_flight_details()

obj2 = Add_person(connection_string)
obj2.use_database()
# obj2.flight_choice_country()
obj2.flight_choice_departure()
obj2.check_flight_capacity()
obj2.check_passenger_count()
obj2.capacity_avaibility()