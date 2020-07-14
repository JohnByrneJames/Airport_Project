import os
from database_connection import DatabaseConnector

# Connection credentials
server = os.environ.get("db_server")  # Server name, this here gets the OS private environment variables
database = "JMS_AirportDatabase"  # Database name, this here gets the OS private environment variables
# Database Login credentials
username = os.environ.get("db_username")  # username, this here gets the OS private environment variables
password = os.environ.get("db_password")  # password, this here gets the OS private environment variables

database_link = DatabaseConnector(server, database, username, password)  # create instance with credentials
database_link.establish_connection()
