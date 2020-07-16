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

SELECT * FROM Flights WHERE FlightID LIKE 4



INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(5,2,'Mariko','Donaldson','477985472','1970-01-26'),(12,2,'Shelly','Ellis','444498640','1973-03-19'),(2,9,'Patrick','Atkinson','134186247','1965-04-01'),(2,17,'Dakota','Cannon','198540183','1990-12-05'),(1,16,'Quentin','Daniels','151774210','1962-09-29'),(1,14,'Steven','Mcintyre','222621031','1975-02-22'),(11,20,'Deirdre','Pickett','874856111','1981-01-07'),(3,18,'Ingrid','Rosa','956704439','1976-05-09'),(13,14,'Theodore','Mccall','080331898','1978-03-12'),(14,14,'Eleanor','Ramsey','497354062','1972-12-01');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(7,2,'Keefe','Bernard','583885298','1985-06-30'),(5,5,'Rudyard','Adkins','281729969','1972-09-21'),(6,15,'Iona','Huffman','762972758','1971-09-15'),(14,15,'Inga','Hood','181221693','1965-10-20'),(4,5,'Jackson','Norman','601123748','1962-02-26'),(10,6,'Orson','Stein','153683253','1992-05-04'),(10,12,'Jarrod','Mathews','550744078','1988-08-14'),(13,16,'Jana','Harvey','953368388','1981-04-08'),(9,19,'Alyssa','Byrd','596310131','1984-09-22'),(11,18,'Hilary','Goodwin','568539531','1957-04-15');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(15,8,'Kaseem','Underwood','396655481','1967-06-09'),(2,14,'Norman','Wilson','641173179','1960-05-02'),(11,17,'Bryar','Britt','853717253','1955-12-10'),(13,8,'Keegan','Pennington','275205726','1977-11-14'),(7,2,'Bevis','Pope','532857761','1980-03-14'),(14,6,'Lavinia','Salazar','721090783','1988-04-19'),(6,19,'Avye','Hardin','836413066','1955-08-09'),(11,13,'Vivian','Jefferson','148886416','1957-02-26'),(5,13,'Haley','Mclean','561749642','1984-07-26'),(4,19,'Cleo','West','456844557','1975-09-16');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(11,19,'Adam','English','282623685','1985-09-13'),(11,13,'Nevada','Marquez','750550690','1987-08-25'),(3,7,'Arden','Newton','428315652','1985-02-18'),(11,14,'Ciara','Middleton','633400326','1956-07-26'),(2,2,'Sasha','Burton','489184174','1989-08-28'),(8,19,'Uma','Warren','525801669','1960-06-23'),(12,15,'Knox','Scott','959066186','1982-01-20'),(15,9,'Cedric','Boyle','611930566','1983-01-20'),(6,13,'Kieran','Gomez','276442072','1985-03-10'),(1,11,'Sawyer','Marsh','436067742','1962-01-05');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(7,1,'Myra','Faulkner','061094562','1970-11-02'),(12,9,'Valentine','Britt','803450510','1957-01-30'),(14,15,'Rebecca','James','418429888','1983-04-23'),(8,9,'Madeline','Simpson','876198982','1963-12-26'),(13,2,'Isaac','Goff','363824848','1960-10-16'),(13,2,'Declan','Hinton','128212034','1963-11-09'),(5,11,'Carlos','Terry','887006987','1957-10-05'),(7,19,'Kiayada','Barnett','552639128','1991-09-11'),(12,14,'Grace','Fowler','362173443','1951-12-25'),(8,11,'Hamilton','Rodriguez','793955485','1957-12-06');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(4,4,'Shannon','Rodriguez','316961202','1982-01-02'),(9,1,'Cyrus','Castaneda','885915125','1969-01-31'),(12,9,'Calvin','Soto','805989727','1965-07-17'),(1,14,'Joelle','Bender','841806130','1969-08-22'),(6,1,'Nissim','Vang','121810900','1962-01-02'),(5,16,'Quyn','Herman','018918062','1960-11-27'),(6,8,'Naomi','Mckinney','134169522','1976-03-31'),(3,15,'Bruno','Bennett','984173179','1987-05-14'),(12,12,'Walter','Powell','871970475','1951-10-05'),(13,7,'Octavia','Simon','408951952','1990-09-18');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(9,13,'Hadassah','Kinney','885588996','1955-12-26'),(1,19,'Adam','Frost','210339388','1983-09-29'),(5,10,'Nissim','Shelton','118779103','1978-05-01'),(8,1,'Kylee','Barnett','270299452','1972-12-31'),(1,11,'Conan','Conner','670473016','1962-09-20'),(7,8,'Kylee','Burgess','262030483','1977-06-19'),(3,16,'Bryar','Griffith','224634469','1953-08-21'),(10,13,'Miriam','Brady','887771599','1984-01-01'),(5,7,'Madison','Simon','225928638','1959-04-21'),(8,3,'Yuli','Sweeney','334362962','1970-10-30');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(13,19,'Colt','Benton','070837483','1963-02-17'),(13,16,'Bruno','Ramirez','176942504','1992-02-18'),(13,4,'Blythe','Calhoun','647202075','1954-03-07'),(10,16,'Ila','Curry','929291885','1965-12-19'),(13,15,'Halla','Bauer','994798112','1978-01-30'),(13,11,'Ashton','Newton','993049755','1978-02-19'),(13,14,'Kimberley','Ballard','510813006','1987-04-29'),(12,8,'Ahmed','Rice','628056241','1983-02-16'),(2,20,'Naomi','Boone','666605092','1989-02-23'),(14,7,'Keefe','Manning','559476289','1959-09-17');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(10,13,'Todd','Ramsey','146933001','1972-09-06'),(9,5,'Alika','Rush','077356447','1960-11-27'),(11,3,'Avye','Young','952781695','1967-04-14'),(11,8,'Xavier','Patel','767852484','1967-02-14'),(12,8,'Ima','Peck','964014403','1986-12-31'),(9,19,'Karen','Church','763581431','1985-07-10'),(7,15,'Stewart','King','963707935','1967-06-13'),(5,18,'Mason','Davenport','438305468','1959-12-22'),(4,19,'Wanda','Riddle','849232321','1974-10-04'),(4,3,'Ishmael','Drake','552781909','1956-03-16');
INSERT INTO BookingDetails([FlightID],[CustomerID],[FirstName],[LastName],[PassportNum],[DateOfBirth]) VALUES(1,19,'Zane','Harrington','818320549','1991-09-11'),(13,14,'Jermaine','Newman','725995706','1979-04-17'),(13,11,'Anika','Lyons','903010232','1988-12-27'),(13,11,'Preston','Kramer','166809516','1964-11-16'),(2,1,'Dakota','Durham','774262363','1958-10-31'),(9,10,'Laura','Perez','715438910','1960-09-17'),(15,5,'Nicholas','Garcia','016677767','1955-01-08'),(4,6,'Erich','Mcdaniel','856331858','1974-08-18'),(1,18,'August','Gross','429157154','1987-01-19'),(7,10,'Fredericka','Larsen','206508769','1965-08-07');
