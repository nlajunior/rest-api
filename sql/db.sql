create database db;

use db;

CREATE TABLE role (
  id int AUTO_INCREMENT,
  name varchar(40) unique NOT NULL,
  actived boolean DEFAULT 1,
  PRIMARY KEY (id)
 
);

CREATE TABLE user (
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

CREATE TABLE device (
  id int NOT NULL AUTO_INCREMENT,
  mac varchar(30) unique NOT NULL,
  date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status varchar(3) NOT NULL DEFAULT 'OFF',
  PRIMARY KEY (id)
);

CREATE TABLE monitor(
   id int NOT NULL AUTO_INCREMENT,
   monitor_id varchar(60) not null unique,
   date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
   status boolean not null default 1,
   device_id varchar(30),
   CONSTRAINT monitor_fk_1 FOREIGN KEY (device_id) REFERENCES device (mac),
   PRIMARY KEY (id)
);

CREATE TABLE test (
  id int NOT NULL AUTO_INCREMENT,
  duration int NOT NULL,
  fhr_value float NOT NULL,
  date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  monitor_id varchar(100) NOT NULL,
  device_id varchar(30) NOT NULL,
  CONSTRAINT test_fk_1 FOREIGN KEY (device_id) REFERENCES device (mac),
  CONSTRAINT test_fk_2 FOREIGN KEY (monitor_id) REFERENCES monitor (monitor_id),
  PRIMARY KEY (id)
);

INSERT INTO `role`(id, name) VALUES (1,'Administrator'),(2,'Customer');

INSERT INTO `user`(login, email, password, organization_key, role) VALUES ('admin','adminapi@sfiecorg.br','N0xdeBrCCKDqQXPALLcAm2}iu^GkBe4','ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&', 1),('userapi','userapi@yourapi.org.br', 'N0xdeBrCCKDqQXPALLcAm2}iu^GkBe4','ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&a',2);

INSERT INTO device (mac) VALUES ('80:7D:3A:DA:D9:F4'),
('80:7D:3A:DA:D9:F5'),
('80:7D:3A:DA:D9:F6'),
('84:0D:8E:17:4D:C8'),
('8C:AA:B5:85:EE:14')
;

#update user set password='N0xdeBrCCKDqQXPALLcAm2}iu^GkBe4' where id=1

select * from role;
select * from user;
select * from device

