import hashlib

# def test()
#     FirstName = input("Enter first name")
#     sql_query = "('INSERT INTO Customers(FirstName, LastName, DateOfBirth) VALUES(" + FirstName + "', 'Smith', '1990/02/06'))"
#     self.cursor.execute(sql_query)

def password_test():
    hash_object = hashlib.sha512(b'password')
    hex_dig = hash_object.hexdigest()
    print(hex_dig)

    password = input('Input string: ')
    staff_password = password.encode('utf-8')
    hash_object2 = hashlib.sha512(staff_password)
    hex_dig2 = hash_object2.hexdigest()
    print(hex_dig2)
    if hex_dig == hex_dig2:
        print("Succes")
    else:
        print("Failure")

password_test()