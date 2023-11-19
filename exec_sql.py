import sql_functions

if __name__ == "__main__":
    conn = sql_functions.create_connection("library.db")
    sql_functions.execute_sql(conn, sql_functions.create_books_sql)
    sql_functions.execute_sql(conn, sql_functions.create_authors_sql)

    sql_functions.delete_all_data(conn, "books")
    sql_functions.delete_all_data(conn, "authors")

    sql_functions.insert_data(conn, "authors", first_name="Michal",
                              last_name="Kaczmarek")
    sql_functions.insert_data(conn, "authors", first_name="Henryk",
                              last_name="Sienkiewicz")
    sql_functions.insert_data(conn, "authors", first_name="Stefan",
                              last_name="Żeromski")

    sql_functions.insert_data(conn, "books", title="test",
                              author_id=1, isbn="1234567890")
    sql_functions.insert_data(conn, "books", title="Krzyzacy",
                              author_id=2, isbn="9876512340")
    sql_functions.insert_data(conn, "books", title="Przedwiosnie",
                              author_id=3, isbn="0987654321")

    sql_functions.update_data(conn, "books", 2, author_id=3, title="test2")

    sql_functions.delete_data(conn, "books", 3)

    sql_functions.select_all_data(conn, "books")

    sql_functions.select_data_where(
        conn, "books", title="test", isbn="1234567890", author_id=1)
