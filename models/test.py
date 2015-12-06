from users import Users
from drivers import Drivers
from map import Map
import create_db


def recreate_db():
    create_db.create_db()
    create_db.create_tables()


d = Drivers()


def test_drivers_assign_order():
    d.assign_order(2, 1)
    d.assign_order(2, 2)
    d.assign_order(3, 3)
    print d.get_orders(1)
    print d.get_orders(2)
    print d.get_orders(3)


def test_drivers_move_1():
    print d.get_available_drivers(1)
    print d.get_available_drivers(2)
    print d.get_available_drivers(3)

    d.start_move(1)
    print d.get_next_point(1)
    d.arrive_to_point(1)
    print d.get_next_point(1)
    print d.get_available_drivers(2)
    d.start_move(1)
    print d.get_available_drivers(2)


def test_drivers_move_2():
    print d.get_next_point(2)
    print d.get_next_point(3)

    print d.get_next_point(1)
    d.start_move(1)
    d.arrive_to_point(1)


m = Map()


def test_map_get_all_cities():
    print m.get_all_cities()
