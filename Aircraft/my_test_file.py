from Database_Connection.database_connection import DatabaseConnector
import os
import datetime as dt

database_link = DatabaseConnector("databases.spartaglobal.academy", "JMS_AirportDatabase",
                                  os.environ.get("db_username"),
                                  os.environ.get("db_password"))  # create instance with credentials
cursor = database_link.establish_connection()  # Use instance to establish connection

# minutes = 510
# minutes_remaining = minutes % 60
# hours = minutes // 60
# print(str(hours) + " Hours " + str(minutes_remaining) + " Minutes")

sql = 'SELECT * FROM Staff'
rows = cursor.execute(sql)

# flight_details = ""
# flight_passengers = ""
# flight_id = ""
#
sql = "SELECT * FROM Flights WHERE FlightID LIKE ?"
rows = cursor.execute(sql, 7)
date_combo = ""

if rows.rowcount == 0:
    print("This flight Id doesnt exist")
else:
    for row in rows:
        flight_id = (str(row.FlightID) + "-" + row.Destination[:3].upper() + "0" +
                     str(row.DepartureDate.day))
        flight_details = (
                (str(row.FlightID) + "-" + row.Destination[:3].upper() + "0" + str(row.DepartureDate.day)) +
                " destined for " + row.Destination + " on " + str(row.DepartureDate.day) + " "
                + str(row.DepartureDate.strftime('%B')) + " " + str(row.DepartureDate.year) + " at "
                + str(row.DepartureTime.strftime('%I:%M %p')) + " travelling to " + row.Destination +
                " with an expected flight time of ")

        date_combo = dt.datetime.combine(row.DepartureDate, row.DepartureTime)
        # Else create new one (Flight ID, Destination [first 3 letters],0 + departureTime[hour])

print(date_combo)

# sql = "SELECT * FROM BookingDetails WHERE FlightID = ?"
# rows = cursor.execute(sql, 7)
#
# print()
#
# counter = 1
#
# if rows.rowcount == 0:
#     print("There are currently no Passengers on this flight")
# else:
#     for row in rows:
#         flight_passengers += ("[" + str(counter) + "]: " + row.FirstName + " " + row.LastName + " | Passport Number : "
#                               + row.PassportNum + "\n")
#         counter += 1
#
#
# # Get date
# now = dt.datetime.now()  # current date and time
#
# # Get suffix of day
# if 4 <= now.day <= 20 or 24 <= now.day <= 30:
#     suffix = "th"
# else:
#     suffix = ["st", "nd", "rd"][now.day % 10 - 1]
#
# # Construct timestamp
# d = now.strftime("Added on the %d" + suffix + " %B %Y, at %I:%M %p")
#
# with open("Generated_Manifests/" + flight_id + ".txt", "w") as file:
#     file.write("Flight Manifest for Flight " + str(flight_id) + "\n\n" + flight_details + "\n\n" +
#                "Passengers on This Flight: \n\n" + flight_passengers + "\n\n" +
#                str(d))


# def password_test():
#     user_pass = input("password")
#     encoded = user_pass.encode("utf-8")
#     hashed_pass = hashlib.sha512(encoded)
#     hashed_pass = hashed_pass.hexdigest()
#     print(type(hashed_pass))
#
# password_test()

# def hash_password(password):
#     # uuid is used to generate a random number
#     # The salt is a random sequence added to the password string before using the hash function. The sale is used
#     # in order to prevent dictionary attacks and rainbow table attacks.
#     salt = uuid.uuid4().hex
#     return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

# def check_password(hashed_password, user_password):
#     password, salt = hashed_password.split(':')
#     return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
#
#
# # This is the retrieved password from the database
# new_pass = input('Please enter a password: ')
# # Hash the password using the hash_password function
# hashing_password = hash_password(new_pass)
# print('The string to store in the db is: ' + hashing_password)
# old_pass = input('Now please enter the password again to check: ')
# if check_password(hashing_password, old_pass):
#     print('You entered the right password')
# else:
#     print('I am sorry but the password does not match')

# sql = 'SELECT * FROM Flights'
# rows = cursor.execute(sql)
#
# dict_of_flights = {}
# counter = 1
#
# for row in rows:
#     dict_of_flights["flight " + str(counter)] = {"Destination": row.Destination,
#                                                  "DepartureDate": row.DepartureDate,
#                                                  "DepartureTime": row.DepartureTime,
#                                                  "FlightDuration": row.FlightDuration,
#                                                  "PassengerLimit": row.PassengerLimit}
#     counter += 1
#
# #longest destionation
# longest_destination = 0
#
# # find destination with longest characters
# for key, value in dict_of_flights.items():
#     print(key, value)
#

# flight_dict = {"Destination": 'gibraltar', "Departure_date": '2018-03-20',
#                "Departure_time": '13:00:00', "Flight_duration": 300,
#                "Passenger_limit": 250}
# #
# print()
#
# sql_query = ("INSERT INTO Flights(Destination, DepartureDate, DepartureTime , FlightDuration, PassengerLimit)"
#              "VALUES(?, ?, ?, ?, ?)")
#
# cursor.execute(sql_query, flight_dict['Destination'], flight_dict['Departure_date'],
#                flight_dict['Departure_time'], flight_dict['Flight_duration'],
#                flight_dict['Passenger_limit'])
#
# cursor.commit()

# sql_query = 'SELECT * FROM Staff WHERE Username LIKE ?'
# lines = cursor.execute(sql_query,)
# rows = lines.fetchall()
# for row in rows:
#     print(row)
#
# sql_query = ('INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit)'
#              'VALUES(?, ?, ?, ?, ?)')
#
# cursor.execute(sql_query, 'GrizzlyLand', '2020-09-29', '13:00:00', 660, 500)
#
# cursor.commit()

# Added to database
# cursor.execute("INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit) "
#                "VALUES('Tokyo', '2020-03-29', '2020-04-05', 660, 500)")

# s = "abc"
#
# contains_digit = any(map(str.isdigit, s))
# print(contains_digit)

# password = ""
# retrieved_username = ""
#
# sql_query = 'SELECT * FROM Staff)'  # WHERE Username LIKE ?'
# rows = cursor.execute(sql_query)
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
