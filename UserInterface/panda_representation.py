#Pandas used in SQL
from Database_Connection.database_connection import DatabaseConnector
import pandas as pd
import pandas.io.sql
import pyodbc

class panda_data:
    def sql_query_with_panda(self):
        server = "databases.spartaglobal.academy"
        database = "JMS_AirportDatabase"
        username = "SA"
        password = "Passw0rd2018"

        connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" \
                            + server + ";DATABASE=" + database + \
                            ";UID=" + username + ";PWD=" + password
        connection = pyodbc.connect(connection_string, autocommit = True)
        # object1 = DatabaseConnector(server,  )
        # cursor = object1.establish_connection()
        # sql_query = ("SELECT * FROM Flights"
        df = pandas.io.sql.read_sql("SELECT * FROM Flights", connection)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(df)


object = panda_data()
object.sql_query_with_panda()

