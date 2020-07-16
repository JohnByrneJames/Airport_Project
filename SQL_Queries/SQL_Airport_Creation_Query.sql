DROP DATABASE JMS_AirportDatabase

SL_HELP 

CREATE DATABASE JMS_AirportDatabase
USE JMS_AirportDatabase

SP_HELP Customers

CREATE TABLE [BookingDetails] (
  [TicketID] Int IDENTITY NOT NULL,
  [FlightID] Int NOT NULL,
  [CustomerID] Int NOT NULL,
  [FirstName] VarChar(200) NOT NULL,
  [LastName] VarChar(200) NOT NULL,
  [PassportNum] VarChar(100) NOT NULL,
  [DateOfBirth] Date NOT NULL,
  PRIMARY KEY ([TicketID]),
  FOREIGN KEY ([FlightID]) REFERENCES Flights(FlightID),
  FOREIGN KEY ([CustomerID]) REFERENCES Customers(CustomerID)
);

CREATE TABLE [Staff] (
  [StaffID] Int IDENTITY NOT NULL,
  [Name] VarChar(200) NOT NULL,
  [Position] VarChar(100) NOT NULL,
  [Username] VarChar(100) NOT NULL,
  [Password] VarChar(100) NOT NULL,
  PRIMARY KEY ([StaffID])
);

CREATE TABLE [Customers] (
  [CustomerID] Int IDENTITY NOT NULL,
  [FirstName] VarChar(200) NOT NULL,
  [LastName] VarChar(200) NOT NULL,
  [DateOfBirth] Date NOT NULL,
  PRIMARY KEY ([CustomerID])
);

CREATE TABLE [Flights] (
  [FlightID] Int IDENTITY NOT NULL,
  [Destination] VarChar(200) NOT NULL,
  [DepartureDate] Date NOT NULL,
  [DepartureTime] Time,
  [FlightDuration] Int NOT NULL,
  [PassengerLimit] Int NOT NULL,
  PRIMARY KEY ([FlightID])
);

ALTER TABLE Flights
ALTER COLUMN DepartureTime Time;

DROP TABLE Flights
DROP TABLE Staff
DROP TABLE BookingDetails
DROP TABLE Customers
DROP TABLE FlightStaff

CREATE TABLE [FlightStaff] (
  [FlightID] Int NOT NULL,
  [StaffID] Int NOT NULL,
  PRIMARY KEY ([FlightID], [StaffID]),
  FOREIGN KEY (FlightID) REFERENCES Flights (FlightID),
  FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
);

SELECT * FROM FlightStaff
SELECT * FROM Customers
SELECT * FROM Flights
SELECT * FROM Staff
SELECT * FROM BookingDetails

SP_HELP Staff
SP_HELP Customers

INSERT INTO Staff(Staff.Name, Staff.Position, Staff.Username, Staff.Password)
VALUES('John', 'Crew-Member', 'J970', '123');

INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit)
VALUES('Boston', '2020-03-29', '13:00:00', 660, 500)
