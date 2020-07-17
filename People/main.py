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
obj1 = Change_details(connection)
# obj1.insert_user_details()
obj1.fetch_current_flight_details()
obj1.show_flight_options_date()
obj1.fetch_flightID()
obj1.change_flight_details()


# Calling functions
# Creating class instance
# obj2 = Add_person(connection)
# obj2.flight_choice_departure()
# obj2.check_flight_capacity()
# obj2.check_passenger_count()
# obj2.capacity_availability()
# obj2.add_person()
# obj2.ticket_sale()

# cursor = connection
# sql_query = "INSERT INTO Customers(FirstName, LastName, DateOfBirth)VALUES('Jeff', 'Smith', '1990/02/06'),('Anna', 'Kendrick', '1972/12/01'),('Robert', 'Happy','1985/06/26'),('Elon', 'Musk', '1982/01/21')"
# cursor.execute(sql_query)
# cursor.commit()