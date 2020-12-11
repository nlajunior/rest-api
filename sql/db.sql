create database db;

use db;

CREATE TABLE role (
  id integer AUTO_INCREMENT,
  name varchar(40) NOT NULL,
  actived tinyint(1) DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY name (name)
);

CREATE TABLE user (
  id int NOT NULL AUTO_INCREMENT,
  login varchar(40) NOT NULL,
  password varchar(200) NOT NULL,
  organization_key varchar(200) NOT NULL,
  email varchar(100) DEFAULT NULL,
  role int DEFAULT NULL,
  actived tinyint(1) DEFAULT 0,
  PRIMARY KEY (id),
  UNIQUE KEY login (login),
  UNIQUE KEY organization_key (organization_key),
  CONSTRAINT user_fk_1 FOREIGN KEY (role) REFERENCES role (id)
);

CREATE TABLE device (
  id int NOT NULL AUTO_INCREMENT,
  mac varchar(100) NOT NULL,
  date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status varchar(3) NOT NULL DEFAULT 'OFF',
  PRIMARY KEY (id)
);

CREATE TABLE test (
  id int NOT NULL AUTO_INCREMENT,
  duration int NOT NULL,
  fhr_value float NOT NULL,
  session_id varchar(100) NOT NULL,
  date_created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  device_id int DEFAULT NULL,
  CONSTRAINT device_fk_1 FOREIGN KEY (device_id) REFERENCES role (id),
  PRIMARY KEY (id)
);

INSERT INTO `role`(id, name) VALUES (1,'Administrator'),(2,'Customer');

INSERT INTO `user`(login, email, password, organization_key, role) VALUES ('admin','adminapi@sfiecorg.br','N0xdeBrCCKDqQXPALLcAm2}iu^GkBe4','ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&', 1),('userapi','userapi@yourapi.org.br', 'N0xdeBrCCKDqQXPALLcAm2}iu^GkBe4','ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&a',2);

INSERT INTO device (mac, status) VALUES ('80:7D:3A:DA:D9:F4','ON'),
('80:7D:3A:DA:D9:F5','ON'),
('80:7D:3A:DA:D9:F6','ON'),
('84:0D:8E:17:4D:C8','ON'),
('8C:AA:B5:85:EE:14','ON')
;
select * from user;
select * from test

upate user set actived=0 where id=1



