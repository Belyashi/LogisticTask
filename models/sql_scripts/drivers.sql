CREATE OR REPLACE FUNCTION get_driver_info(driver_id INT)
  RETURN SYS_REFCURSOR
  AS
  drivers_info_cursor SYS_REFCURSOR;
BEGIN
  OPEN drivers_info_cursor FOR SELECT
      user_id,
      capacity,
      (select name from Cities where id=Drivers.last_city_id and ROWNUM <= 1),
      on_way
    FROM Drivers
    WHERE id = driver_id;
  RETURN drivers_info_cursor;
END;


CREATE OR REPLACE FUNCTION get_driver_id(userr_id INT)
  RETURN INT
  AS
  driver_id INT;
BEGIN
  SELECT id INTO driver_id FROM Drivers WHERE user_id = userr_id;
  RETURN driver_id;
END;


CREATE OR REPLACE FUNCTION get_available_drivers(city_id INT)
  RETURN SYS_REFCURSOR
  AS
  available_drivers SYS_REFCURSOR;
BEGIN
  OPEN available_drivers FOR
    SELECT (id,capacity)
      FROM Drivers
        WHERE on_way = FALSE AND (last_city_id = city_id OR last_city_id = NULL);
  RETURN available_drivers;
END;


CREATE OR REPLACE FUNCTION get_orders(driv_id INT)
  RETURN SYS_REFCURSOR
  AS
  orders_cursor SYS_REFCURSOR;
BEGIN
  OPEN orders_cursor FOR SELECT
      id, delivered, count,
      (SELECT name FROM Organizations WHERE id=Orders.customer_id AND ROWNUM <= 1),
      (SELECT name FROM Goods WHERE id=Orders.goods_id AND ROWNUM <= 1)
    FROM Orders WHERE id in (SELECT order_id FROM DriversOrders WHERE driver_id=driv_id);
  RETURN orders_cursor;
END;


CREATE OR REPLACE FUNCTION get_next_point(driv_id INT)
  RETURN SYS_REFCURSOR
  AS
  point_cursor SYS_REFCURSOR;
BEGIN
  OPEN point_cursor FOR SELECT * FROM (SELECT
      t1.id, t2.start_city_id, t2.finish_city_id,
      (SELECT name FROM Cities WHERE id=t2.start_city_id) AS start_city,
      (SELECT name FROM Cities WHERE id=t2.finish_city_id) AS finish_city
    FROM Routes t1
      INNER JOIN Ways t2
          ON t1.way_id = t2.id
    WHERE t1.driver_id = driv_id AND t1.performed = 'N'
    ORDER BY t1.id)
    WHERE ROWNUM <= 1;
END;


CREATE OR REPLACE PROCEDURE set_on_way(driv_id INT, moving BOOLEAN) AS
  BEGIN
    IF (moving) THEN
      UPDATE Drivers SET on_way = 'Y' WHERE id = driv_id;
    ELSE
      UPDATE Drivers SET on_way = 'N' WHERE id = driv_id;
    END IF;
  END;


CREATE OR REPLACE PROCEDURE start_move(driv_id INT) AS
  next_point INT;
  BEGIN
    next_point := get_next_point(driv_id);
    IF NOT (next_point IS NULL) THEN
      set_on_way(driv_id, TRUE);
    END IF;
  END;


CREATE OR REPLACE PROCEDURE make_performed_next_point(driv_id INT) AS
  BEGIN
    UPDATE Routes SET performed = 'Y'
    WHERE id = (
      SELECT MIN(id) FROM (
        SELECT id
        FROM Routes
        WHERE driver_id = driv_id AND performed = 'N'
      )
    );
  END;


CREATE OR REPLACE PROCEDURE set_last_city_id(driv_id INT, l_city_id INT) AS
  BEGIN
    UPDATE Drivers SET last_city_id = l_city_id WHERE id = driv_id;
  END;


CREATE OR REPLACE PROCEDURE unload_orders(driv_id INT, fin_city_id INT) AS
  BEGIN
    UPDATE DriversOrders t1
      INNER JOIN Orders t2
         ON t1.order_id = t2.id
      INNER JOIN Organizations t3
         ON t2.customer_id = t3.id
    SET t2.delivered = 'Y'
    WHERE t1.driver_id = driv_id AND t3.city_id = fin_city_id;
  END;


CREATE OR REPLACE PROCEDURE arrive_to_point(driv_id INT) AS
  next_point INT;
  fin_city_id INT;
  BEGIN
    next_point := get_next_point(driv_id);
    if not (next_point IS NULL) THEN
      make_performed_next_point(driv_id);

      SELECT finish_city_id INTO fin_city_id FROM Ways WHERE id=next_point;

      set_last_city_id(driv_id, fin_city_id);
      set_on_way(driv_id, FALSE);
      unload_orders(driv_id, fin_city_id);
    END IF;
  END;