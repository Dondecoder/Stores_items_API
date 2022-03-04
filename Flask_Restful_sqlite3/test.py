import sqlite3

connection = sqlite3.connect('data.db')


cursor = connection.cursor() # cursor is responsible for executing the queries and storing into a database. It runs a query and store result

create_table = "CREATE TABLE users (id int, username text, password text)"


cursor.execute(create_table)


user = (1, 'jose', 'asdf')

insert_query = "INSERT INTO users VALUES (?,?,?)"


cursor.execute(insert_query,user)

users = [

    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print (row)

connection.commit() # to save to the database 

connection.close() # means that the database will not receive anymore resources as it waits for data 