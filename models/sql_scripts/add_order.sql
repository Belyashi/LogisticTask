INSERT INTO Orders
(customer_id, delivered)
VALUES (%s, FALSE)

INSERT INTO OrdersGoods
(order_id, good_id, count)
VALUES ((SELECT MAX(id) FROM Orders), %s, %s);
