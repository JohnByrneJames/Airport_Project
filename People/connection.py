import os
import pyodbc

class Connection:

    # Intiliasing class
    def __init__(self, connection_string):
        self.connection_string = connection_string

    # Create function to intialise connection
    def create_connection(self):
        # Try except loop to connect to server
        try:
            with pyodbc.connect(self.connection_string, timeout=20) as connection:
                print("Connection worked")
        except:
            print("Connection timed out")
        # Creating connection
        self.connection = connection
        return self.connection

    # Create function to intialise cursor
    def create_cursor(self):
        # Creating and returning cursor
        self.cursor = self.connection.cursor()
        return self.cursor

    def use_database(self):
        # Calling previous methods and specifing what database to use
        self.create_connection()
        self.create_cursor()
        self.cursor.execute("use JMS_AirportDatabase")
