from sql_functions import *

conn = create_connection("library.db")
execute_sql(conn, create_books_sql)
execute_sql(conn, create_authors_sql)

delete_all_data(conn, "books")
delete_all_data(conn, "authors")

insert_data(conn, "books", title="test",
            author_id=1, isbn="1234567890")
insert_data(conn, "books", title="Krzyzacy",
            author_id=2, isbn="9876512340")
insert_data(conn, "books", title="Przedwiosnie",
            author_id=3, isbn="0987654321")

insert_data(conn, "authors", first_name="Michal",
            last_name="Kaczmarek")
insert_data(conn, "authors", first_name="Henryk",
            last_name="Sienkiewicz")
insert_data(conn, "authors", first_name="Stefan",
            last_name="Żeromski")

update_data(conn, "books" , 2, author_id=3, title="test2")

delete_data(conn, "books", 3)

select_all_data(conn, "books")

select_data_where(conn, "books", title="test", isbn="1234567890", author_id=1)
