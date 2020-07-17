#Pandas used in SQL
from Database_Connection.database_connection import DatabaseConnector
import pandas as pd
import pandas.io.sql
import pyodbc
class panda_data:
    def sql_query_with_panda(self):
        data_connection = DatabaseConnector("databases.spartaglobal.academy", "JMS_AirportDatabase", "SA",
                                  "Passw0rd2018")
        conn = data_connection.establish_connection()
        # object1 = DatabaseConnector(server,  )
        # cursor = object1.establish_connection()
        # sql_query = ("SELECT * FROM Flights"
        df = pandas.io.sql.read_sql("SELECT * FROM Flights", conn)
        conn.commit()
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(df)
