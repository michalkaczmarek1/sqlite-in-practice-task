import sqlite3
from sqlite3 import Error


create_authors_sql = """
    CREATE TABLE IF NOT EXISTS authors (
        id integer PRIMARY KEY,
        first_name varchar(50) NOT NULL,
        last_name varchar(50) NOT NULL
    );
"""

create_books_sql = """
    CREATE TABLE IF NOT EXISTS books (
        id integer PRIMARY KEY,
        author_id integer NOT NULL,
        title varchar(50) NOT NULL,
        isbn varchar(15) NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors (id) 
    );
"""


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def execute_sql(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def insert_data(conn, table, **kwargs):
    try:
        columns = [f"{k}" for k in kwargs]
        columns = ", ".join(columns)
        parameters = [f"?" for v in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        sql = f"INSERT INTO {table}({columns}) VALUES({parameters})"
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
    except Error as e:
        print(e)


def update_data(conn, table, id, **kwargs):
    parameters = [f"{k}=?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )
    sql = f''' UPDATE {table}
                SET {parameters}
                WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)


def delete_data(conn, table, id):
    values = (id, )
    sql = f''' DELETE FROM {table}
                WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)


def delete_all_data(conn, table):
    sql = f'DELETE FROM {table}'
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)


def select_all_data(conn, table):
    sql = f'SELECT * FROM {table}'
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        print("OK")
    except Error as e:
        print(e)


def select_data_where(conn, table, **kwargs):
    parameters = [f"{k}=?" for k in kwargs]
    parameters = " AND ".join(parameters)
    values = tuple(v for v in kwargs.values())
    sql = f"SELECT * FROM {table} WHERE {parameters}"
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        rows = cur.fetchall()
        print(rows)
        print("OK")
    except Error as e:
        print(e)
