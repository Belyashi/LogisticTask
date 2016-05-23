CREATE OR REPLACE PROCEDURE reduce(good_id INT, good_count INT) IS
  refcursor SYS_REFCURSOR;
  cur_residue INT;
  BEGIN
    OPEN refcursor FOR
        SELECT residue FROM Goods WHERE id=good_id;
    FETCH refcursor INTO cur_residue;
    IF (res < good_count) THEN
      raise_application_error(-20101, 'Reduced count must be not less than existing.');
    END IF;
    UPDATE Goods
      SET residue=(cur_residue - good_count)
    WHERE id=good_id;
  END;

CREATE OR REPLACE FUNCTION get_all_goods
RETURN SYS_REFCURSOR IS
  refcursor SYS_REFCURSOR;
  BEGIN
    OPEN refcursor FOR
      SELECT id, name, price, producer_id, weight, residue
        FROM Goods
          WHERE residue > 0;
    RETURN refcursor;
  END;