create database dreamhome_team;
use dreamhome_team;

desc staff;
desc branch;
desc privateowner;
desc propertyforrent;
desc `client`;


create table staff(
	staff_no varchar(6)primary key,
    fname varchar(15),
    lname varchar(15), 
    sex char(1),
    dob date,
    branch_no char(6),
    pos varchar(20),
    salary numeric(6),
    supervisor_no varchar(5),
    manager_date date,
    manager_bonus numeric(6)
);

ALTER TABLE staff 
MODIFY COLUMN staff_no varchar(6);
ALTER TABLE staff 
MODIFY COLUMN branch_no varchar(6);


create table BRANCH(
	branch_no varchar (6) primary key,
	address varchar(100),
	telNo varchar(20)
);
ALTER TABLE branch
MODIFY COLUMN branch_no varchar(6);
ALTER TABLE branch
MODIFY COLUMN address varchar(100) not null;

ALTER TABLE branch ADD CONSTRAINT unique_address UNIQUE (address);


create table `client`(
	clientNo char(6) primary key,
	fname varchar(30),
    lname varchar(30),
	regBranch varchar(6),
	regStaff varchar(6),
	prefType varchar(10),
	maxRent int,
    regDate date
);
ALTER TABLE `client` 
MODIFY COLUMN clientNo varchar(6);
ALTER TABLE `client` 
MODIFY COLUMN regStaff varchar(6);

create table PrivateOwner(
	OwnerNo char(6) primary key,
    ownerName varchar(30),
    homeAddress varchar(100),
    telNo char(15),
    regBranch varchar(6),
    regStaff varchar(6),
    regDate date,
    typeOfBusiness varchar(20),
    contactName varchar(40)
);
ALTER TABLE privateOwner 
MODIFY COLUMN regStaff varchar(6);
ALTER TABLE privateOwner MODIFY COLUMN homeAddress varchar(100) not null;
ALTER TABLE PrivateOwner ADD CONSTRAINT unique_address UNIQUE (homeAddress);


create table propertyForRent(
	 propertyNo char(6) primary key,
	 propType varchar(10),
     rooms smallint,
	 rent int,
	 address varchar(100),
	 regOwner varchar(6) not null,
	 regStaff varchar(6),
	 regBranch varchar(6),
     regDate date
);
ALTER TABLE propertyforrent 
MODIFY COLUMN regBranch varchar(6);
ALTER TABLE propertyforrent MODIFY COLUMN address varchar(100) not null;
ALTER TABLE propertyforrent ADD CONSTRAINT unique_address UNIQUE (address);


SELECT * FROM BRANCH;
SELECT * FROM STAFF;
select * from `client`;
SELECT * FROM PRIVATEOWNER;
SELECT * FROM PROPERTYFORRENT;

-- 1
ALTER TABLE staff
ADD CONSTRAINT
FOREIGN KEY (branch_no)
REFERENCES branch(branch_no) on delete cascade on update cascade;

-- 2
ALTER TABLE `client`
ADD CONSTRAINT
FOREIGN KEY (regBranch)
REFERENCES branch(branch_no) on delete cascade on update cascade;

ALTER TABLE `client`
ADD CONSTRAINT
FOREIGN KEY (regStaff)
REFERENCES staff(staff_no) on delete cascade on update cascade;

-- 3
ALTER TABLE PrivateOwner
ADD CONSTRAINT
FOREIGN KEY (regBranch)
REFERENCES branch(branch_no) on delete cascade on update cascade;

ALTER TABLE PrivateOwner
ADD CONSTRAINT
FOREIGN KEY (regStaff)
REFERENCES staff(staff_no) on delete cascade on update cascade;

-- 4
ALTER TABLE PropertyForRent
ADD CONSTRAINT
FOREIGN KEY (regStaff)
REFERENCES staff(staff_no) on delete cascade on update cascade;

ALTER TABLE PropertyForRent
ADD CONSTRAINT
FOREIGN KEY (regBranch)
REFERENCES branch(branch_no) on delete cascade on update cascade;

ALTER TABLE PropertyForRent
ADD CONSTRAINT
FOREIGN KEY (regOwner)
REFERENCES privateowner(ownerno) on delete cascade on update cascade;

select * from propertyforrent;

create table view_report(
	propertyNo varchar(6) not null,
    clientNo varchar(6) not null,
    view_date date not null,
    comment varchar(256)
);
alter table view_report add constraint foreign key (clientNo) references `client`(clientNo) on delete cascade on update cascade;
-- not null constraints 
-- branch_no in staff

