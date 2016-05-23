CREATE OR REPLACE FUNCTION get_organization_id (userr_id INT)
  RETURN INT
  AS
  org_id INT;
BEGIN
  SELECT id INTO org_id FROM Organizations WHERE user_id = userr_id;
  RETURN org_id;
END;


CREATE OR REPLACE FUNCTION get_goods(org_id INT)
  RETURN SYS_REFCURSOR
  AS
  curs SYS_REFCURSOR;
BEGIN
  OPEN curs FOR SELECT id FROM Goods WHERE producer_id = org_id;
  RETURN curs;
END;


CREATE OR REPLACE PROCEDURE add_good(name VARCHAR2(100), price INT, organization_id INT, weight INT, residue INT)
  AS
BEGIN
  INSERT INTO Goods
  (name, price, producer_id, weight, residue)
  VALUES (name, price, organization_id, weight, residue);
END;


CREATE OR REPLACE FUNCTION get_orders(org_id INT)
  RETURN SYS_REFCURSOR
  AS
  org_orders SYS_REFCURSOR;
BEGIN
  OPEN org_orders FOR SELECT id, delivered, count,
      (SELECT name FROM Goods WHERE id=Orders.goods_id)
      FROM Orders
      WHERE customer_id = org_id;
  RETURN org_orders;
END;

CREATE OR REPLACE FUNCTION check_overflow_count(good_id INT, cnt INT)
  RETURN BOOLEAN AS
  count INT;
BEGIN
  SELECT residue INTO count FROM Goods WHERE id = good_id;
  IF (cnt > count) THEN
    RETURN TRUE;
  ELSE
    RETURN FALSE;
  END IF;
END;


CREATE OR REPLACE FUNCTION get_producer_city_id(good_id INT)
  RETURN INT
  AS
  producer_city_id INT;
BEGIN
  SELECT city_id
  INTO producer_city_id
  FROM Organizations
  WHERE id =
  (SELECT producer_id FROM Goods WHERE id = good_id and ROWNUM <= 1);
  RETURN producer_city_id;
END;


CREATE OR REPLACE FUNCTION get_driver_for_deliver(city_id INT)
  RETURN INT AS
  driver_id INT;
BEGIN
  SELECT id INTO driver_id
  FROM Drivers
  WHERE last_city_id = city_id
  AND on_way = 'N' and ROWNUM <= 1;
  RETURN driver_id;
END;


CREATE OR REPLACE PROCEDURE assign_order(driv_id INT, ord_id INT) is
  BEGIN
    INSERT INTO DriversOrders
    (driver_id, order_id)
    VALUES (driv_id, ord_id);
  END;