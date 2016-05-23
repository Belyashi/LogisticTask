CREATE TABLE Users (
  id INT NOT NULL,
  login VARCHAR2(20) NOT NULL UNIQUE,
  pass VARCHAR2(64) NOT NULL,
  CONSTRAINT users_pk PRIMARY KEY (id)
);

CREATE SEQUENCE users_id_sequence;

CREATE OR REPLACE TRIGGER generate_user_id
  BEFORE INSERT ON Users
  FOR EACH ROW
  BEGIN
    :NEW.id := users_id_sequence.nextval;
  END;

--------------------------------------------------

CREATE TABLE Cities (
  id INT NOT NULL,
  name VARCHAR2(20) NOT NULL,
  CONSTRAINT cities_pk PRIMARY KEY (id)
);

CREATE SEQUENCE cities_id_sequence;

CREATE OR REPLACE TRIGGER generate_city_id
  BEFORE INSERT ON Cities
  FOR EACH ROW
  BEGIN
    :NEW.id := cities_id_sequence.nextval;
  END;

--------------------------------------------------

CREATE TABLE Organizations (
  id INT NOT NULL,
  name VARCHAR2(20) NOT NULL,
  user_id INT NOT NULL,
  city_id INT NOT NULL,
  CONSTRAINT organizations_id PRIMARY KEY (id),
  CONSTRAINT user_id_fk_organizations FOREIGN KEY (user_id) REFERENCES Users(id),
  CONSTRAINT city_id_fk_organizations FOREIGN KEY (city_id) REFERENCES Cities(id)
);

CREATE SEQUENCE organizations_id_sequence;

CREATE OR REPLACE TRIGGER generate_organization_id
  BEFORE INSERT ON Organizations
  FOR EACH ROW
  BEGIN
    :NEW.id := organizations_id_sequence.nextval;
  END;

--------------------------------------------------

CREATE TABLE Drivers (
  id INT NOT NULL,
  user_id INT NOT NULL,
  capacity INT NOT NULL,
  last_city_id INT NOT NULL,
  on_way CHAR(1) DEFAULT 'N' NOT NULL,
  CONSTRAINT drivers_pk PRIMARY KEY (id),
  CONSTRAINT user_id_fk_drivers FOREIGN KEY (user_id) REFERENCES Users(id),
  CONSTRAINT last_city_id_fk_drivers FOREIGN KEY (last_city_id) REFERENCES Cities(id)
);

CREATE SEQUENCE drivers_id_sequence;

CREATE OR REPLACE TRIGGER generate_driver_id
  BEFORE INSERT ON Drivers
  FOR EACH ROW
  BEGIN
    :NEW.id := drivers_id_sequence.nextval;
  END;

--------------------------------------------------

CREATE TABLE Goods (
  id INT NOT NULL,
  name VARCHAR2(20) NOT NULL,
  price INT NOT NULL,
  producer_id INT NOT NULL,
  weight INT NOT NULL,
  residue INT NOT NULL,
  CONSTRAINT goods_pk PRIMARY KEY (id),
  CONSTRAINT producer_id_fk_goods FOREIGN KEY (producer_id) REFERENCES Organizations(id)
);

CREATE SEQUENCE goods_id_sequence;

CREATE OR REPLACE TRIGGER generate_good_id
  BEFORE INSERT ON Goods
  FOR EACH ROW
  BEGIN
    :NEW.id := goods_id_sequence.nextval;
  END;

--------------------------------------------------

CREATE TABLE Orders (
  id INT NOT NULL,
  customer_id INT NOT NULL,
  delivered CHAR(1) DEFAULT 'N' NOT NULL,
  goods_id INT NOT NULL,
  count INT NOT NULL,
  CONSTRAINT orders_pk PRIMARY KEY (id),
  CONSTRAINT customer_id_fk_orders FOREIGN KEY (customer_id) REFERENCES Organizations(id),
  CONSTRAINT goods_id_fk_orders FOREIGN KEY (goods_id) REFERENCES Goods(id)
);

CREATE SEQUENCE orders_id_sequence;

CREATE OR REPLACE TRIGGER generate_order_id
  BEFORE INSERT ON Orders
  FOR EACH ROW
  BEGIN
    :NEW.id := orders_id_sequence.nextval;
  END;

--------------------------------------------------

CREATE TABLE DriversOrders (
  driver_id INT NOT NULL,
  order_id INT NOT NULL,
  CONSTRAINT drivers_orders_pk PRIMARY KEY (driver_id, order_id),
  CONSTRAINT driver_id_fk_drivers_orders FOREIGN KEY (driver_id) REFERENCES Drivers(id),
  CONSTRAINT order_id_fk_drivers_orders FOREIGN KEY (order_id) REFERENCES Orders(id)
);

--------------------------------------------------

CREATE TABLE Ways (
  id INT NOT NULL,
  start_city_id INT NOT NULL,
  finish_city_id INT NOT NULL,
  length INT NOT NULL,
  CONSTRAINT ways_pk PRIMARY KEY (id),
  CONSTRAINT start_city_id_fk_ways FOREIGN KEY (start_city_id) REFERENCES Cities(id),
  CONSTRAINT finish_city_id_fk_ways FOREIGN KEY (finish_city_id) REFERENCES Cities(id)
);

CREATE SEQUENCE ways_id_sequence;

CREATE OR REPLACE TRIGGER generate_way_id
  BEFORE INSERT ON Ways
  FOR EACH ROW
  BEGIN
    :NEW.id := ways_id_sequence.nextval;
  END;

--------------------------------------------------

CREATE TABLE Routes (
  id INT NOT NULL,
  driver_id INT NOT NULL,
  way_id INT NOT NULL,
  performed CHAR(1) DEFAULT 'N' NOT NULL,
  CONSTRAINT routes_pk PRIMARY KEY (id),
  CONSTRAINT driver_id_fk_routes FOREIGN KEY (driver_id) REFERENCES Drivers(id),
  CONSTRAINT way_id_fk_routes FOREIGN KEY (way_id) REFERENCES Ways(id)
);

CREATE SEQUENCE routes_id_sequence;

CREATE OR REPLACE TRIGGER generate_route_id
  BEFORE INSERT ON Routes
  FOR EACH ROW
  BEGIN
    :NEW.id := routes_id_sequence.nextval;
  END;