create database db;

use db;

CREATE TABLE db.role (
  id int AUTO_INCREMENT,
  name varchar(40) unique NOT NULL,
  actived boolean DEFAULT 1,
  PRIMARY KEY (id)
 
)

CREATE TABLE db.log_error (
  id int AUTO_INCREMENT,
  device_id varchar(30),
  date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  level_error int,
  message varchar(100),
  PRIMARY KEY(id)
);

CREATE TABLE db.user (
  id int NOT NULL AUTO_INCREMENT,
  login varchar(40) unique NOT NULL,
  password varchar(200) NOT NULL,
  organization_key varchar(200) unique NOT NULL,
  email varchar(100),
  role int NOT NULL,
  actived boolean DEFAULT 0,
  PRIMARY KEY (id), 
  CONSTRAINT user_fk_1 FOREIGN KEY (role) REFERENCES role (id)
);


CREATE TABLE db.device (
  id int NOT NULL AUTO_INCREMENT,
  mac varchar(30) unique NOT NULL,
  date_created datetime DEFAULT CURRENT_TIMESTAMP,
  status varchar(3) NOT NULL DEFAULT 'OFF',
  PRIMARY KEY (id)
);

CREATE TABLE db.monitoring(
   id int NOT NULL AUTO_INCREMENT,
   identifier varchar(60) not null unique,
   date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
   status boolean not null default 1,
   device_id varchar(30),
   CONSTRAINT monitoring_fk_1 FOREIGN KEY (device_id) REFERENCES device (mac),
   PRIMARY KEY (id)
);

CREATE TABLE db.test (
  id int NOT NULL AUTO_INCREMENT,
  duration int NOT NULL,
  fhr_value float NOT NULL,
  date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  identifier varchar(60) NOT NULL,
  device_id varchar(30) NOT NULL,
  CONSTRAINT test_fk_1 FOREIGN KEY (device_id) REFERENCES device (mac),
  CONSTRAINT test_fk_2 FOREIGN KEY (identifier) REFERENCES monitoring (identifier),
  PRIMARY KEY (id)
);

create user 'user_api'@'localhost' identified with mysql_native_password by 'EqV#j1ooc7^7Fv9}-x9c#m^39vavbNFZy,eeK:NA';
grant select, insert, update, delete, execute on db.* to 'user_api'@'localhost' ;
#=====================================================================================================================================================================================================================================================================================================================================================
#INSERT INTO `role`(id, name) VALUES (1,'Administrator'),(2,'Customer');
#INSERT INTO `user`(login, email, password, organization_key, role) VALUES ('admin','adminapi@sfiecorg.br','N0xdeBrCCKDqQXPALLcAm2}iu^GkBe4','ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&', 1),('userapi','userapi@yourapi.org.br', 'N0xdeBrCCKDqQXPALLcAm2}iu^GkBe4','ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&a',2);
#INSERT INTO db.device (mac) VALUES 
#('80:7D:3A:DA:D9:F4'),
#('80:7D:3A:DA:D9:F5'),
#('80:7D:3A:DA:D9:F6'),
#('84:0D:8E:17:4D:C8'),
#('8C:AA:B5:85:EE:14')
#;
#insert into db.device(mac) values('8C:AA:B5:85:XX')
#insert into db.monitoring (identifier, device_id) values('8C:AA:B5:85:EE:14:1','8C:AA:B5:85:EE:14');
#insert into db.test (duration, fhr_value, date_created, identifier, device_id) values(5, 120, '2020-12-15', '80:7D:3A:DA:D9:F5:1', '80:7D:3A:DA:D9:F5');
#insert into db.test (duration, fhr_value, date_created, identifier, device_id) values(10, 126, '2020-12-15', '80:7D:3A:DA:D9:F5:1', '80:7D:3A:DA:D9:F5');
#insert into db.monitoring (identifier, device_id) values('80:7D:3A:DA:D9:F4:1','80:7D:3A:DA:D9:F4');
#insert into db.test (duration, fhr_value, identifier, device_id) values(15, 120.5, '8C:AA:B5:85:EE:14:1', '8C:AA:B5:85:EE:14');
#=====================================================================================================================================================================================================================================================================================================================================================
#select * from db.role;
#select * from db.user;
#select * from db.device;
#select * from db.monitoring;
#select * from db.test;
#select * from db.log_error;
#SELECT * FROM db.test where DATE_FORMAT(date_created, '%Y-%m-%d')='2021-01-18' ORDER BY id DESC LIMIT 14;

#explain format=JSON SELECT identifier from db.monitoring order by identifier desc limit 1;
#explain format=json select(id), identifier from db.monitoring order by id desc limit 1;

#explain format=json SELECT t.duration, t.fhr_value, t.identifier FROM db.test as t inner join db.monitoring as m on t.identifier=m.identifier
#WHERE t.IDENTIFIER='80:7D:3A:DA:D9:F5:1' AND DATE_FORMAT(t.date_created, '%Y-%m-%d')='2020-12-15' AND t.duration>=0 AND t.duration<=200 AND m.status=1 \G

#explain format=json SELECT t.duration, t.fhr_value, t.identifier FROM db.test as t inner join db.monitoring as m on t.identifier=m.identifier
#WHERE t.IDENTIFIER='80:7D:3A:DA:D9:F5:1' AND DATE_FORMAT(t.date_created, '%Y-%m-%d')='2021-01-11' AND t.duration>=0 AND t.duration<=200 AND m.status=1

#show variables where variable_name like '%dir'
#update db.monitoring set status=1 where id=1
 
#alter table db.test drop foreign key test_fk_2;
#alter table db.test modify device_id varchar(30) null



select duration, fhr_value, date_created, identifier, device_id from db.test ORDER BY duration LIMIT 4 OFFSET 2

SELECT duration, fhr_value, identifier FROM db.test 
WHERE identifier='AAAEGAAAAK' 
AND DATE_FORMAT(date_created, '%Y-%m-%d')='2021-01-27' 
AND duration>=5 AND duration<=100 
ORDER BY duration asc LIMIT 50 

SELECT duration, fhr_value, identifier FROM db.test
WHERE DATE_FORMAT(date_created, '%Y-%m-%d')='2021-01-27' AND duration>=5 AND duration<=100
ORDER BY identifier, duration asc LIMIT 50

SELECT duration, fhr_value, identifier FROM db.test
WHERE identifier in('AAACDAFAAK','AAACDCFAAM') AND DATE_FORMAT(date_created, '%Y-%m-%d')='2021-01-27' AND duration>=5 AND duration<=50
ORDER BY identifier, duration asc LIMIT 50



















