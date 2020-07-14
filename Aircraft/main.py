import os
from database_connection import DatabaseConnector

database_link = DatabaseConnector(os.environ.get("db_server"), "JMS_AirportDatabase", os.environ.get("db_username"),
                                  os.environ.get("db_password"))  # create instance with credentials
database_link.establish_connection()  # Use instance to establish connection
