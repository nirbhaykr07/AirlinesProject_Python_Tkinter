CREATE TABLE "passengers" (
	"customerId"	TEXT NOT NULL,
	"firstName"	TEXT,
	"lastName"	TEXT,
	"DOB"	TEXT,
	"Mobile"	TEXT,
	"Gender"	TEXT,
	"Address"	TEXT,
	"Password"	TEXT,
	PRIMARY KEY("customerId")
);

CREATE TABLE "flights" (
	"source"	TEXT,
	"dest"	TEXT,
	"date"	TEXT,
	"seats"	INTEGER,
	"price"	INTEGER,
	"company"	TEXT,
	"flight_num"	TEXT NOT NULL,
	PRIMARY KEY("flight_num")
);

CREATE TABLE "tickets" (
	"CustomerId"	TEXT NOT NULL,
	"FlightName"	TEXT,
	"FlightNumber"	TEXT NOT NULL,
	"FlightDate"	TEXT,
	"FlightFare"	INTEGER,
	"Source"	TEXT,
	"Dest"	TEXT,
	"Tickets"	INTEGER,
	FOREIGN KEY("CustomerId") REFERENCES "passengers"("customerId")
);

insert  into flights values('delhi','patna','10/7/10',10,1000,'Indigo',"A12345")
insert  into flights values('blr','delhi','10/7/10',10,1000,'Indigo',"B12345")
insert  into flights values('chennai','kochi','10/7/10',10,1000,'Indigo',"C12345")
insert  into flights values('kochi','chennai','10/7/10',10,1000,'Indigo',"D12345")
insert  into flights values('chennai','blr','10/7/10',10,1000,'Indigo',"E12345")
insert  into flights values('blr','patna','10/7/10',10,1000,'Indigo',"F12345")
insert  into flights values('patna','chennai','10/7/10',10,1000,'Indigo',"G12345")
insert  into flights values('chennai','delhi','10/7/10',10,1000,'Indigo',"H12345")
insert  into flights values('patna','kochi','10/7/10',10,1000,'Indigo',"J12345")
insert  into flights values('kochi','patna','10/7/10',10,1000,'Indigo',"K12345")
insert  into flights values('delhi','kochi','10/7/10',10,1000,'Indigo',"L12345")
insert  into flights values('mumbai','patna','10/7/10',10,1000,'Indigo',"M12345")
insert  into flights values('mumbai','delhi','10/7/10',10,1000,'Indigo',"N12345")
insert  into flights values('delhi','mumbai','10/7/10',10,1000,'Indigo',"O12345")
