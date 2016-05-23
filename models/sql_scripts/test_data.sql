SELECT id, name, price, producer_id, weight, residue FROM Goods where residue>0;
INSERT INTO Cities (name) VALUES ('ohoho');
SELECT * FROM Cities;
INSERT INTO DriversOrders (driver_id, order_id) VALUES (5, 8);
SELECT *
FROM DriversOrders;

INSERT INTO Cities (name) VALUES ('Minsk');
INSERT INTO Cities (name) VALUES ('Gomel');
INSERT INTO Cities (name) VALUES ('Vitebsk');
INSERT INTO Cities (name) VALUES ('Soligosrk');
INSERT INTO Cities (name) VALUES ('Grodno');

INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 2, 100);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 4, 50);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 5, 120);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (2, 3, 200);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (2, 4, 300);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (3, 5, 10);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (2, 1, 100);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (4, 1, 50);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (5, 1, 120);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (3, 2, 200);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (4, 2, 300);
INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (5, 3, 10);

--passwords
INSERT INTO Users (login, pass) VALUES ('vasia', 'a8ea357a8595a0479744e23171f5935e5abbe5a1dcfd3752ae2c4c39');  --123
INSERT INTO Users (login, pass) VALUES ('masha', 'b7e718e93f99931c468f94d648636153bc3d7960384d8a87f9941c61');  --1234
INSERT INTO Users (login, pass) VALUES ('petia', '4f3045a771449645f86b4fb47313186b1214cfa448af7cf78cf9835a');  --321
INSERT INTO Users (login, pass) VALUES ('sasha', 'dcd0a6fc86fc0274ce90e2e1c6799295474cffbedf9c4d0bcf6581cd');  --111
INSERT INTO Users (login, pass) VALUES ('ivan', '0ddaf435b2c3f0d6c5eb18d1f17b4058f9c0264a7599179fd8617b93');   --121

INSERT INTO Users (login, pass) VALUES ('userus', '451d0956af24514beb2908fd75eb3f607480253be5c584d335058937'); --4321
INSERT INTO Users (login, pass) VALUES ('wtf', '741fa3f576d7ef09202356a7cd2d5bff59fc986d2e70357aaddd2eb8');    --wtf
INSERT INTO Users (login, pass) VALUES ('kolia', '0ddaf435b2c3f0d6c5eb18d1f17b4058f9c0264a7599179fd8617b93');  --121
INSERT INTO Users (login, pass) VALUES ('lesha', 'dcd0a6fc86fc0274ce90e2e1c6799295474cffbedf9c4d0bcf6581cd');  --111
INSERT INTO Users (login, pass) VALUES ('dima', 'a8ea357a8595a0479744e23171f5935e5abbe5a1dcfd3752ae2c4c39');   --123

INSERT INTO Users (login, pass) VALUES ('driver1234', 'b7e718e93f99931c468f94d648636153bc3d7960384d8a87f9941c61'); --1234
INSERT INTO Users (login, pass) VALUES ('driver4321', '451d0956af24514beb2908fd75eb3f607480253be5c584d335058937'); --4321
INSERT INTO Users (login, pass) VALUES ('driverwtf', '741fa3f576d7ef09202356a7cd2d5bff59fc986d2e70357aaddd2eb8');  --wtf


INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (1, 100, 1);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (3, 150, 2);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (5, 200, 1);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (7, 200, 3);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (8, 170, 4);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (9, 180, 5);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (10, 140, 2);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (11, 180, 3);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (12, 210, 4);
INSERT INTO Drivers (user_id, capacity, last_city_id) VALUES (13, 228, 5);


INSERT INTO Organizations (name, user_id, city_id) VALUES ('OOO SuperTovari', 2, 4);
INSERT INTO Organizations (name, user_id, city_id) VALUES ('BlaBla and Co', 4, 2);
INSERT INTO Organizations (name, user_id, city_id) VALUES ('MyCompany', 6, 1);

INSERT INTO Goods (name, price, producer_id, weight, residue) VALUES ('kniga', 1, 1, 10, 20);
INSERT INTO Goods (name, price, producer_id, weight, residue) VALUES ('stol', 3, 1, 30, 20);
INSERT INTO Goods (name, price, producer_id, weight, residue) VALUES ('ruchka', 2, 2, 10, 20);