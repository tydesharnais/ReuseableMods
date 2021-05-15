import sqlite3

with sqlite3.connect('waldo.db') as db:
	cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
userID INTERGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL,
email VARCHAR(20) NOT NULL,
ipaddr VARCHAR(20) NOT NULL);
""")

cursor.execute("""
INSERT INTO user(username,firstname,surname,password,email,ipaddr)
VALUES("test_user", "Bob", "Smith", "MrBob", "mrbob@gmail.com", "137.159.157.144")
""")
db.commit()

cursor.execute("SELECT * FROM user")

print(cursor.fetchall())
