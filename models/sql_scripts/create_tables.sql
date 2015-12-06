CREATE TABLE Users (
  id INT NOT NULL AUTO_INCREMENT,
  login VARCHAR(20) NOT NULL,
  pass VARCHAR(20) NOT NULL,
  PRIMARY KEY (id, login)
);

CREATE TABLE Cities(
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Organizations (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(20) NOT NULL,
  user_id INT NOT NULL,
  city_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES Users(id),
  FOREIGN KEY (city_id) REFERENCES Cities(id)
);

CREATE TABLE Drivers (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  capacity INT NOT NULL,
  last_city_id INT NOT NULL,
  on_way BOOL NOT NULL DEFAULT FALSE,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES Users(id),
  FOREIGN KEY (last_city_id) REFERENCES Cities(id)
);

CREATE TABLE Goods (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(20) NOT NULL,
  price INT NOT NULL,
  producer_id INT NOT NULL,
  weight INT NOT NULL,
  residue INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (producer_id) REFERENCES Organizations(id)
);

CREATE TABLE Orders (
  id INT NOT NULL AUTO_INCREMENT,
  customer_id INT NOT NULL,
  delivered BOOL NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES Organizations(id)
);

CREATE TABLE OrdersGoods (
  order_id INT NOT NULL,
  goods_id INT NOT NULL,
  count INT NOT NULL,
  PRIMARY KEY (order_id, goods_id),
  FOREIGN KEY (order_id) REFERENCES Orders(id),
  FOREIGN KEY (goods_id) REFERENCES Goods(id)
);

CREATE TABLE DriversOrders (
  driver_id INT NOT NULL,
  order_id INT NOT NULL,
  PRIMARY KEY (driver_id, order_id),
  FOREIGN KEY (driver_id) REFERENCES Drivers(id),
  FOREIGN KEY (order_id) REFERENCES Orders(id)
);

CREATE TABLE Ways (
  id INT NOT NULL AUTO_INCREMENT,
  start_city_id INT NOT NULL,
  finish_city_id INT NOT NULL,
  length INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (start_city_id) REFERENCES Cities(id),
  FOREIGN KEY (finish_city_id) REFERENCES Cities(id)
);

CREATE TABLE Routes (
  id INT NOT NULL AUTO_INCREMENT,
  driver_id INT NOT NULL,
  way_id INT NOT NULL,
  performed BOOL NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (driver_id) REFERENCES Drivers(id),
  FOREIGN KEY (way_id) REFERENCES Ways(id)
);