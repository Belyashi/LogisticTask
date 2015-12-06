INSERT INTO Cities (name) VALUES ("Minsk");
INSERT INTO Cities (name) VALUES ("Gomel");
INSERT INTO Cities (name) VALUES ("Vitebsk");
INSERT INTO Cities (name) VALUES ("Soligosrk");
INSERT INTO Cities (name) VALUES ("Grodno");

INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 2, 100);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 4, 50);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 5, 120);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (2, 3, 200);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (2, 4, 300);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (3, 5, 10);

INSERT INTO Users (login, pass) VALUES ("vasia", "123");
INSERT INTO Users (login, pass) VALUES ("masha", "1234");
INSERT INTO Users (login, pass) VALUES ("petia", "321");
INSERT INTO Users (login, pass) VALUES ("sasha", "111");
INSERT INTO Users (login, pass) VALUES ("ivan", "121");

INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (1, 100, 1);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (3, 150, 2);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (4, 200, 1);

INSERT INTO Organizations (name, user_id, city_id) VALUES ("OOO SuperTovari", 2, 3);
INSERT INTO Organizations (name, user_id, city_id) VALUES ("BlaBla and Co", 4, 1);

INSERT INTO Orders (customer_id, delivered) VALUES (1, FALSE );
INSERT INTO Orders (customer_id, delivered) VALUES (1, FALSE );
INSERT INTO Orders (customer_id, delivered) VALUES (1, TRUE );
INSERT INTO Orders (customer_id, delivered) VALUES (2, FALSE );
INSERT INTO Orders (customer_id, delivered) VALUES (2, FALSE );

INSERT INTO Routes (driver_id, way_id, performed) VALUES (1, 1, FALSE );
INSERT INTO Routes (driver_id, way_id, performed) VALUES (1, 5, FALSE );
INSERT INTO Routes (driver_id, way_id, performed) VALUES (3, 4, TRUE );