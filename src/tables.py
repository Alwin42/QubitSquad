import sqlite3

conn = sqlite3.connect("../property.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS PROPERTIES (PROPERTY_ID INTEGER NOT NULL PRIMARY KEY, PROPERTY_NAME TEXT, IS_OWNED INTEGER)''')

cursor.close()
conn.close()

conn = sqlite3.connect("../users.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME TEXT, PASSWORD TEXT, FULLNAME TEXT, PROPERTY_ID INTEGER, FOREIGN KEY(PROPERTY_ID) REFERENCES USERS(PROPERTY_ID))''')

cursor.close()
conn.close()
