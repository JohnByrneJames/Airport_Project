import pyodbc

def databaseconnection(self):
    server = 'databases2.spartaglobal.academy'
    database = 'JMS_AirportDatabase'
    username = 'SA'
    password = 'Passw0rd2018'
    connections = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    # This is to initalising the connection of the server and connecting the database to Python. This will allow us to manipulate the data and execute python commands.

    self.cursor = connections.cursor()
    print("Connection successful")
    return self.cursor  # Takes the variable, running the method will be this output.

    # This is assigning and creating the cursor from the connection.

    # Create function to intialise cursor
def use_database(self):
    self.cursor.execute("use JMS_AirportDatabase")



