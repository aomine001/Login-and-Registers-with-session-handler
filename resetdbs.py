import sqlite3
import os

os.system('del SESSION.db')
os.system('del users.db')

SESSIONDB = sqlite3.connect('SESSION.db')
DBCURSOR = SESSIONDB.cursor()

USERDB = sqlite3.connect('users.db')
USERCURSOR = USERDB.cursor()

sql = 'CREATE TABLE session (ip varchar(2048) NOT NULL, uuid varchar(2048) NOT NULL, user varchar(65535) NOT NULL);' #uuid = user unique id log n pwd
sql2 = 'CREATE TABLE users (log varchar(65535) NOT NULL, pwd varchar(25565) NOT NULL, banned varchar(8) NOT NULL)'

DBCURSOR.execute(sql)
SESSIONDB.commit()

USERCURSOR.execute(sql2)
USERDB.commit()

print('Success, reseted database.')
SESSIONDB.close()
USERDB.close()
