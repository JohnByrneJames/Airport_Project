from connection import Connection

class Add_person(Connection):

    def __init__(self, connection_string):
        # Inheriting connection string from parent class
        super().__init__(connection_string)
        self.ticket_price = 3.00

    def flight_choice(self):
        pass
        # List countries
        # User input to select country

    def check_capacity(self):
        pass

    def add_person(self):
        pass

    def ticket_sale(self):
        pass
