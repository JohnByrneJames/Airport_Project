from passengerinput import Passengers
from new_connection import databaseconnection

cursor = databaseconnection()
object = cursor.Passengers(databaseconnection())
object.passenger_input()
