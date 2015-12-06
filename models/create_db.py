import MySQLdb
import config


def create_db():
    db = MySQLdb.connect(host=config.HOST,
                         user=config.USER,
                         passwd=config.PASSWD)
    db.query("DROP DATABASE " + config.NAME)
    db.query("CREATE DATABASE " + config.NAME)
    db.commit()
    db.close()


def create_tables():
    db = MySQLdb.connect(host=config.HOST,
                         user=config.USER,
                         passwd=config.PASSWD,
                         db=config.NAME)
    with open("./sql_scripts/create_tables.sql", "r") as f:
        sql = f.read()
    cur = db.cursor()
    cur.execute(sql)
    cur.close()
    db.close()

def make_test_data():
    db = MySQLdb.connect(host=config.HOST,
                         user=config.USER,
                         passwd=config.PASSWD,
                         db=config.NAME)

    cur = db.cursor()

    cur.execute('INSERT INTO Cities (name) VALUES ("Minsk")')
    cur.execute('INSERT INTO Cities (name) VALUES ("Gomel")')
    cur.execute('INSERT INTO Cities (name) VALUES ("Vitebsk")')
    cur.execute('INSERT INTO Cities (name) VALUES ("Soligosrk")')
    cur.execute('INSERT INTO Cities (name) VALUES ("Grodno")')

    cur.execute('INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 2, 100)')
    cur.execute('INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 4, 50)')
    cur.execute('INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (1, 5, 120)')
    cur.execute('INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (2, 3, 200)')
    cur.execute('INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (2, 4, 300)')
    cur.execute('INSERT INTO Ways (start_city_id, finish_city_id, length) VALUES (3, 5, 10)')

    cur.execute('INSERT INTO Users (login, pass) VALUES ("vasia", "123")')
    cur.execute('INSERT INTO Users (login, pass) VALUES ("masha", "1234")')
    cur.execute('INSERT INTO Users (login, pass) VALUES ("petia", "321")')
    cur.execute('INSERT INTO Users (login, pass) VALUES ("sasha", "111")')
    cur.execute('INSERT INTO Users (login, pass) VALUES ("ivan", "121")')

    cur.execute('INSERT INTO Drivers (user_id, capacity, location_city_id) VALUES (1, 100, 4)')
    cur.execute('INSERT INTO Drivers (user_id, capacity, location_city_id) VALUES (3, 150, 1)')
    cur.execute('INSERT INTO Drivers (user_id, capacity, location_city_id) VALUES (4, 200, 4)')

    cur.execute('INSERT INTO Organizations (name, user_id, city_id) VALUES ("OOO SuperTovari", 2, 3)')
    cur.execute('INSERT INTO Organizations (name, user_id, city_id) VALUES ("BlaBla and Co", 4, 1)')

    cur.execute('INSERT INTO Orders (customer_id, delivered) VALUES (1, FALSE )')
    cur.execute('INSERT INTO Orders (customer_id, delivered) VALUES (1, FALSE )')
    cur.execute('INSERT INTO Orders (customer_id, delivered) VALUES (1, TRUE )')
    cur.execute('INSERT INTO Orders (customer_id, delivered) VALUES (2, FALSE )')
    cur.execute('INSERT INTO Orders (customer_id, delivered) VALUES (2, FALSE )')

    db.commit()
    cur.close()
    db.close()

import sys

if len(sys.argv) > 1 and sys.argv[1] == 'create':
    create_db()
    create_tables()
    make_test_data()
