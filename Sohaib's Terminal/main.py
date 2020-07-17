from passengerinput import Passengers
from Database_Connection.database_connection import DatabaseConnector

datalink = DatabaseConnector("databases.spartaglobal.academy", "JMS_AirportDatabase", "SA", "Passw0rd2018")

cursor = datalink.establish_connection()
object = Passengers(cursor)
object.customer_input()
object.choice_input()

# object.customer_booking_itself()

object2 =