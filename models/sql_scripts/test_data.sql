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

##passwords
INSERT INTO Users (login, pass) VALUES ("vasia", "a8ea357a8595a0479744e23171f5935e5abbe5a1dcfd3752ae2c4c39");  ##123
INSERT INTO Users (login, pass) VALUES ("masha", "b7e718e93f99931c468f94d648636153bc3d7960384d8a87f9941c61");  ##1234
INSERT INTO Users (login, pass) VALUES ("petia", "4f3045a771449645f86b4fb47313186b1214cfa448af7cf78cf9835a");  #321
INSERT INTO Users (login, pass) VALUES ("sasha", "dcd0a6fc86fc0274ce90e2e1c6799295474cffbedf9c4d0bcf6581cd");  #111
INSERT INTO Users (login, pass) VALUES ("ivan", "0ddaf435b2c3f0d6c5eb18d1f17b4058f9c0264a7599179fd8617b93");   #121
INSERT INTO Users (login, pass) VALUES ("userus", "451d0956af24514beb2908fd75eb3f607480253be5c584d335058937"); #4321

INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (1, 100, 1);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (3, 150, 2);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (4, 200, 1);

INSERT INTO Organizations (name, user_id, city_id) VALUES ("OOO SuperTovari", 2, 4);
INSERT INTO Organizations (name, user_id, city_id) VALUES ("BlaBla and Co", 4, 2);
INSERT INTO Organizations (name, user_id, city_id) VALUES ("MyCompany", 6, 1);

INSERT INTO Goods (name, price, producer_id, weight, residue) VALUES ('kniga', 1, 1, 10, 20);
INSERT INTO Goods (name, price, producer_id, weight, residue) VALUES ('stol', 3, 1, 30, 20);
INSERT INTO Goods (name, price, producer_id, weight, residue) VALUES ('ruchka', 2, 2, 10, 20);

INSERT INTO Orders (customer_id, goods_id, count) VALUES (1, 1, 1);
INSERT INTO Orders (customer_id, goods_id, count) VALUES (1, 2, 3);
INSERT INTO Orders (customer_id, delivered, goods_id, count) VALUES (1, TRUE, 3, 10);
INSERT INTO Orders (customer_id, goods_id, count) VALUES (2, 3, 4);
INSERT INTO Orders (customer_id, goods_id, count) VALUES (2, 2, 2 );

INSERT INTO DriversOrders (driver_id, order_id) VALUES (1, 1);
INSERT INTO DriversOrders (driver_id, order_id) VALUES (1, 4);

INSERT INTO Routes (driver_id, way_id, performed) VALUES (1, 1, FALSE );
INSERT INTO Routes (driver_id, way_id, performed) VALUES (1, 5, FALSE );
INSERT INTO Routes (driver_id, way_id, performed) VALUES (3, 4, TRUE );