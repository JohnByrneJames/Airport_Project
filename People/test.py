def test()
    FirstName = input("Enter first name")
    sql_query = "('INSERT INTO Customers(FirstName, LastName, DateOfBirth) VALUES(" + FirstName + "', 'Smith', '1990/02/06'))"
    self.cursor.execute(sql_query)

