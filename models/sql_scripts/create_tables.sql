CREATE TABLE Cities (
    id int not null AUTO_INCREMENT,
    name varchar(20) not null,
    PRIMARY KEY (id)
);

CREATE TABLE Drivers (
    id int not null AUTO_INCREMENT,
    name varchar(20) not null,
    PRIMARY KEY (id)
);

CREATE TABLE Producers (
    id int not null AUTO_INCREMENT,
    name varchar(20) not null,
    city_id int not null,
    PRIMARY KEY (id),
    FOREIGN KEY (city_id) REFERENCES Cities(id)
);

CREATE TABLE Consumers (
    id int not null AUTO_INCREMENT,
    name varchar(20) not null,
    city_id int not null,
    PRIMARY KEY (id),
    FOREIGN KEY (city_id) REFERENCES Cities(id)
);

CREATE TABLE Roots (
    id int not null AUTO_INCREMENT,
    travel_time time,
    travel_length int,
    PRIMARY KEY (id)
);
  
CREATE TABLE Cities_Roots (
    city_id int not null,
    root_id int not null,
    FOREIGN KEY (city_id) REFERENCES Cities(id),
    FOREIGN KEY (root_id) REFERENCES Roots(id),
    PRIMARY KEY (city_id, root_id)
);
  
CREATE TABLE Ways (
    id int not null AUTO_INCREMENT,
	travel_time time,
	travel_length int,
    city2_id int not null,
    city1_id int not null,
    PRIMARY KEY (id),
    FOREIGN KEY (city2_id) REFERENCES Cities(id),
    FOREIGN KEY (city1_id) REFERENCES Cities(id)
);
  
CREATE TABLE Roots_Ways (
    id int not null AUTO_INCREMENT,
    root_id int not null,
    way_id int not null,
    PRIMARY KEY (id),
    FOREIGN KEY (root_id) REFERENCES Roots(id),
    FOREIGN KEY (way_id) REFERENCES Ways(id)
);
  
CREATE TABLE Orders (
    id int not null AUTO_INCREMENT,
	status varchar(20) not null,
    driver_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (driver_id) REFERENCES Drivers(id)
);
  
CREATE TABLE Goods (
    id int not null AUTO_INCREMENT,
	name varchar(20) not null,
    order_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (order_id) REFERENCES Orders(id)
);
