from passengerinput import Passengers
from new_connection import databaseconnection

cursor = databaseconnection()

object = Passengers(cursor)
# object.customer_input()
object.choice_input()