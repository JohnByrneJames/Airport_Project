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
  [DepartureTime] DateTime,
  [FlightDuration] Int NOT NULL,
  [PassengerLimit] Int NOT NULL,
  PRIMARY KEY ([FlightID])
);

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

-- Renamed column in Flights table
-- sp_rename 'Flights.FlightTime', 'FlightDuration';

-- insert into flights
INSERT INTO Flights(Destination, DepartureDate, DepartureTime, FlightDuration, PassengerLimit)
VALUES ('London', '2019/09/21', '13:23', 120, 300);

-- insert into staf
INSERT INTO Staff(Name, Position, Username, Password)
VALUES('Robert', 'Crew member', 'Ro8912', '123')

INSERT INTO Staff(Name, Position, Username, Password)
VALUES('Alex', 'Crew member', 'Al1566', '123'),
('Rachel', 'Crew member', 'Ra3882', '123'),
('Michel', 'Crew member', 'Mi0931', '123')

SELECT f.Username, f.Password
FROM Staff f
WHERE f.Username LIKE 'Al1566'

SELECT * FROM Flights

SP_HELP Flights
SP_HELP Staff

ALTER TABLE Flights
ALTER COLUMN DepartureTime time; 

ALTER TABLE Staff
DROP COLUMN FlightID