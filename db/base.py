import sqlite3
from pathlib import Path


def db_init():
    """Для инициализации соединения с БД sqlite"""
    PROJECT_DIR = Path(__file__).parent.parent
    DB_FILE = 'db.sqlite'
    global db, cur
    db = sqlite3.connect(PROJECT_DIR / DB_FILE)
    cur = db.cursor()
    print("БД создана")


def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        photo TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY,
        user_name TEXT,
        address TEXT,
        product_id INTEGER,
        FOREIGN KEY (product_id) 
            REFERENCES products (product_id)
            ON DELETE CASCADE
    )""")
    db.commit()


def delete_tables():
    cur.execute("""DROP TABLE IF EXISTS products""")
    db.commit()


def populate_products():
    cur.execute("""INSERT INTO products (name, price, photo) VALUES 
                            ('Кот Томас', 20000, 'images/imgpreview.jpg'),
                            ('Кот Гарфилд', 30000, 'images/orig.jpg')
    """)
    db.commit()


def get_products():
    cur.execute("""SELECT * FROM products""")
    all_products = cur.fetchall()
    print(all_products)
    return all_products


if __name__ == "__main__":
    db_init()
    delete_tables()
    create_tables()
    populate_products()
    get_products()
