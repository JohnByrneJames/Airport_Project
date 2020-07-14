from connection import Connection
import os

# Defining database username etc variables
server = os.environ.get('db_server')
database = "JMS_AirportDatabase"
username = os.environ.get('db_username')
password = os.environ.get('db_password')

# Creating connections string object with variables
connection_string = ('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


# Calling functions
# Creating class instance
obj1 = Connection(connection_string)
obj1.create_connection()