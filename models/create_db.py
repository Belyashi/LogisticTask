import MySQLdb
import config

def create_bd():
	db = MySQLdb.connect(host = config.HOST,
			     user = config.USER,
			     passwd = config.PASSWD)
	db.query("DROP DATABASE " + config.NAME)
	db.query("CREATE DATABASE " + config.NAME)
	db.commit()
	db.close()

def create_tables():
	db = MySQLdb.connect(host = config.HOST,
			     user = config.USER,
			     passwd = config.PASSWD,
			     db = config.NAME)
	with open("./sql_scripts/create_tables.sql", "r") as f:
		sql = f.read()
	cur = db.cursor()
	cur.execute(sql)
	cur.close()
	db.close()

create_bd()
create_tables()
