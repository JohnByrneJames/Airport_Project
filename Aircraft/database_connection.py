import pyodbc

class DatabaseConnector:
    # Essential attributes needed by database connector to make a connection {Server, Database, Username, Password}
    # Connection_string formulated using credentials and then a cursor that is used to make the retrieval of data from
    # the database.
    __server = None
    __database = None
    __username = None
    __password = None
    __connection_string = None
    __cursor = None
    retry_timer = 0

    def __init__(self, server, database, username, password):
        self.__server = server
        self.__database = database
        self.__username = username
        self.__password = password
        self.retry_timer = 0  # This is used to count the attempts to connect to the database

    def establish_connection(self):  # establishing connection
        # Create, store and connect to the database using this connection string
        connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" \
                           + self.__server + ";DATABASE=" + self.__database + \
                           ";UID=" + self.__username + ";PWD=" + self.__password
        self.__connection_string = connection_string

        try:
            with pyodbc.connect(self.__connection_string, timeout=10) as connection:  # Connection to database
                # Success and connection has been made
                print("Connection successfully established..!")  # Connection has been established, continue.
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):  # Catch common errors faced in pyodbc
            return "connection has timed out, or the database was not available - " \
                   "\nNo point in retrying... Please review connection credentials"
        except pyodbc.InterfaceError:
            # This is an error that is raised when the database interface is not available.
            print("Invalid connection to DB interface")
            print("\nTrying again...")  # Try reconnecting to the database again.
            if self.retry_timer == 3:  # After 2 attempts exit
                return "Error encountered"
            self.retry_timer += 1  # Increase the retry timer by 1
            self.establish_connection()  # retry establishing connection by calling itself
        except Exception:  # base Exception makes this fall proof
            # This prevents exceptions falling through the exceptions handler (as this catches all possible exceptions)
            return "There was an error that occurred during the connection attempt..."
        else:
            cursor = connection.cursor()  # The cursor is a control structure

