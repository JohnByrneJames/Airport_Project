import os
from database_connection import DatabaseConnector
from flight_interface import FlightFrontEnd

database_link = DatabaseConnector(os.environ.get("db_server"), "JMS_AirportDatabase", os.environ.get("db_username"),
                                  os.environ.get("db_password"))  # create instance with credentials
connection = database_link.establish_connection()  # Use instance to establish connection

user_login = FlightFrontEnd(connection)  # Create users login instance, with previously made connection
user_login.user_login()  # Attempt login
