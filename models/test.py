from drivers import Drivers
from map import Map
from models.db import create_db
from organizations import Organizations


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


def test_get_driver_id():
    print d.get_driver_id(4)


m = Map()


def test_map_get_all_cities():
    print m.get_all_cities()

def test_map_get_all_ways():
    print m.get_all_ways()

o = Organizations()


def test_get_organization_id():
    print o.get_organization_id(2)


def test_organization_orders():
    print o.get_orders(1)
    print o.get_orders(2)
    print o.get_orders(3)

    o.add_order(3, 2, 3)
    print o.get_orders(3)


def test_organization_goods():
    print o.get_goods(1)
    print o.get_goods(2)
    print o.get_goods(3)

    o.add_goods('telephon', 1500, 3, 20, 30)
    print o.get_goods(3)

test_map_get_all_ways()