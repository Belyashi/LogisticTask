from users import Users
from drivers import Drivers
import create_db


def recreate_db():
    create_db.create_db()
    create_db.create_tables()

d = Drivers()
# d.assign_order(2, 1)
# d.assign_order(2, 2)
# d.assign_order(3, 3)
# print d.get_orders(1)
# print d.get_orders(2)
# print d.get_orders(3)

# print d.get_available_drivers(1)
# print d.get_available_drivers(2)
# print d.get_available_drivers(3)

# print d.get_available_drivers(2)
# d.start_move(1)
# print d.get_next_point(1)
# d.arrive_to_point(1)
# print d.get_next_point(1)
# print d.get_available_drivers(2)
# d.start_move(1)
# print d.get_available_drivers(2)
#
# print d.get_next_point(2)
# print d.get_next_point(3)