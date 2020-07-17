import hashlib

class CreateStaffUser:
    staff_name = None
    staff_position = None
    staff_username = None
    staff_password = None
    staff_password_encrypted = None

    def __init__(self, cursor):
        self.cursor = cursor

    def user_creation(self):
        # Take details on staff name
        self.staff_name = input("What is your name?\n")
        self.staff_position = input("What is your position?\n")
        # Using initials to create user name
        self.staff_username = (self.staff_name[0:3]).upper() + (self.staff_position[0])
        self.password_creator()

    def password_creator(self):
        # Get user input for password
        print("\nA password should be at least 7 characters long\n")
        # Check password is certain length, using try except loop
        try:
            self.staff_password = input("Enter you password here\n")
            if len(self.staff_password) > 7:
                pass
            else:
                raise ValueError("incorrect")
        except ValueError:
            print("\nYour password is not long enough, make sure it is 7 characters")
        except Exception:
            print("Error")
        # Using if loop to check password is same when retyped.
        staff_password_check = input("Enter your password again\n")
        # If loop to verify password using double entry
        if staff_password_check == self.staff_password:
            print("\nYour password has been set, make sure to remember it")
        else:
            print("\nThat was not correct, please recreate your password")
            self.password_creator()
        self.encrypt_password()

    def encrypt_password(self):
        # Encoding initial variable
        self.staff_password = self.staff_password.encode('utf-8')
        # Hashing password
        hash_object = hashlib.sha256(self.staff_password)
        self.staff_password_encrypted = hash_object.hexdigest()

    def insert_user_details(self):
        # Calling previous method to ensure user details are created
        self.user_creation()
        # Creating SQL query with wild cards to be placeholders
        sql_query = "INSERT INTO Staff(Name, [Position], Username, password)VALUES (?, ?, ?, ?)"
        # Executing query with variables put in.
        self.cursor.execute(sql_query, self.staff_name, self.staff_position, self.staff_username,
                            str(self.staff_password_encrypted))
        # Committing query to make sure data has been inputted
        self.cursor.commit()
        # Printing success message
        print("\nYour user details have successfully been inputted")
