from users import Users
import create_db


def recreate_db():
    create_db.create_db()
    create_db.create_tables()

