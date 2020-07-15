from database_connection import DatabaseConnector
from string import ascii_letters, digits  # Check for special characters
import os

# database_link = DatabaseConnector(os.environ.get("db_server"), "JMS_AirportDatabase", os.environ.get("db_username"),
#                                   os.environ.get("db_password"))  # create instance with credentials
# cursor = database_link.establish_connection()  # Use instance to establish connection

# cursor.execute('SELECT * FROM Flights')
# cursor.execute("INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit)"
#                "VALUES('Boston', '2020-03-29', '13:00:00', 660, 500)")
# cursor.commit()

# Added to database
# cursor.execute("INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit) "
#                "VALUES('Tokyo', '2020-03-29', '2020-04-05', 660, 500)")

s = "abc"

contains_digit = any(map(str.isdigit, s))
print(contains_digit)

# password = ""
# retrieved_username = ""
# username = 'Ro8912'

# sql_query = 'SELECT * FROM Staff WHERE Username LIKE ?'
# lines = cursor.execute(sql_query, username)
# rows = lines.fetchall()
# # rows = cursor.execute(sql)
# for row in rows:
#     password = row.Password
#     retrieved_username = row.Username

# print(password)
# print(retrieved_username)

# sql_query = 'SELECT FirstName, LastName FROM Employees WHERE FirstName LIKE ?'
# lines = cursor.execute(sql_query, 'Anne')
# rows = lines.fetchall()
# for row in rows:
#     print(row)

# sql_query = 'SELECT * FROM Staff WHERE Username LIKE ?'
# cursor.execute("USE JMS_AirportDatabase")
# lines = cursor.execute(sql_query, 'Ro8912')
# rows = lines.fetchall()
# for row in rows:
#     print(row)

