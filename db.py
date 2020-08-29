import sqlite3
from sqlite3 import Error


def create_connection():
    try:
        conn = sqlite3.connect('data.db')
        return conn
    except Error as e:
        print(e)


def create_table():
    with create_connection() as conn:
        sql = """
        CREATE TABLE IF NOT EXISTS items (
            name text,
            done int
        )
        """
        cursor = conn.cursor()
        cursor.execute(sql)


def save(name, done):
    with create_connection() as conn:
        sql = """
            INSERT into items VALUES (?, ?)
            """
        cursor = conn.cursor()
        cursor.execute(sql, (name, done))
        conn.commit()

    return cursor.lastrowid


def select():
    with create_connection() as conn:
        sql = """
            SELECT * FROM items
            """
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        new_rows = [dict(zip(['name', 'done'], row)) for row in rows]
    return new_rows


def update(done, rowid):
    with create_connection() as conn:
        sql = """
            update items set done = ? where rowid = ?
            """
        cursor = conn.cursor()
        cursor.execute(sql, (done, rowid))
        conn.commit()
    return rowid


def delete(rowid):
    with create_connection() as conn:
        sql = """
            delete from items where rowid = ?
            """
        cursor = conn.cursor()
        cursor.execute(sql, [rowid])
        conn.commit()
    return rowid


# create_connection()

# create_table()

# print(save('界面与布局', 0))
# print(save('界面与布局', 0))

# print(select())

# print(update(1, 1))

# print(delete(3))