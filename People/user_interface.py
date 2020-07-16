# from x import y



class User_interface():

    def __init__(self):
        self.user_interface_visual()

    # Creating a good user interface with print commands
    def user_interface_visual(self):
        print("   Virtual Aircraft Terminal\n======================================")
        print("Welcome to the virtual aircraft terminal, would you like to access customer or staff programs?")


    def intial_input(self):
        user_input = input("Enter C for customer programs or S for staff programs\n")
        if user_input.upper() == "S":
            self.staff_greetings()
        elif user_input.upper() == "C":
            self.customer_greetings()
        else:
            print("Sorry that is an invalid input")
            self.intial_input()

    def staff_greetings(self):
        print("Available staff member programs are:")
        user_input = int(input("1. Creating flight details\n2. Changing existing flight details\n3. Adding a passenger to a flight\n4. Generate a flight attendees list \n5. Create a password and username\n"))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            pass
        else:
            print("Sorry that is an invalid input")
            self.staff_greetings()

    def customer_greetings(self):
        print("Available customer programs are:")
        user_input = int(input(
            "1. Book tickets\n2. View current flights\n"))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        else:
            print("Sorry that is an invalid input")
            self.customer_greetings()


obj1 = User_interface()
obj1.intial_input()
