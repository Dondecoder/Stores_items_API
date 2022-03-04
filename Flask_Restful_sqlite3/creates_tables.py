import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" # in order to create auto increment columns use 
# INTEGER PRIMARY KEY to use auto incrementation. You can use int instead of integer primary key but do not expect auto incrementation if you add more things to your
# database 
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" # real just means a number with a decimal
cursor.execute(create_table)

connection.commit()
connection.close()