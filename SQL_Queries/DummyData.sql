USE Northwind
USE JMS_AirportDatabase

ALTER TABLE Flights
ALTER COLUMN DepartureTime time;

SELECT * FROM Flights
SP_HELP Flights

INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit)
VALUES 
('London', '2019/09/21', '13:23', 120, 300),
('Paris', '2019/01/10', '09:15', 80, 250),
('Rome', '2019/10/07', '12:45', 150, 280),
('Lyon', '2019/01/10', '09:15', 80, 250),
('Moscow', '2019/01/10', '09:15', 60, 250),
('Berlin', '2020/09/01', '15:20', 240, 250)

SELECT * FROM BookingDetails
SP_HELP BookingDetails
INSERT INTO BookingDetails(FlightID, CustomerID, FirstName,LastName, PassportNum, DateOfBirth)
VALUES
(1, 1, 'Jeff', 'Smith', '123456', '1990/02/06'),
(1, 1, 'Morty', 'Smith', '123457', '1999/09/10'),
(3, 2, 'Liam', 'Neeson', '123458', '1992/06/26'),
(4, 2, 'Anna', 'Kendrick', '111132', '1972/12/01'),
(5, 3, 'Bob', 'Lonely', '120921', '1987/07/05'),
(5, 4, 'Ali', 'Johnson', '136542', '1995/02/05'),
(6, 4, 'Theresa', 'May', '123456', '1990/02/06'),
(6, 4, 'Ellie', 'Johnson', '123456', '2005/02/06'),
(6, 4, 'Eleanor', 'Johnson', '123456', '2005/02/06')

SELECT * FROM Customers
SP_HELP Customers

INSERT INTO Customers(FirstName, LastName, DateOfBirth)
VALUES
('Jeff', 'Smith', '1990/02/06'),
('Anna', 'Kendrick', '1972/12/01'),
('Robert', 'Happy', '1985/06/26'),
('Elon', 'Musk', '1982/01/21')

