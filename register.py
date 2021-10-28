import sqlite3
import hashlib

def word_in(s):
   return " " not in s

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

def checkuser(user,con,cur):
    this_connection = con
    this_cursor = cur
    this_user = user

    sql_code = 'SELECT * FROM users WHERE log="'+this_user+'"'

    this_cursor.execute(sql_code)
    this_connection.commit()

    rows = cursor.fetchall()
    founduser = len(rows)

    if founduser != 0:
        print("user already exists")
        _=input()
        exit()

    return True
def createuser(log,pwd,con,cur):
    this_login = log
    this_password = pwd
    this_connection = con
    this_cursor = cur


    to_hash = str(this_password).encode('utf-8')
    hash = hashlib.md5(to_hash).hexdigest()

    sql_code = 'INSERT INTO users (log,pwd,banned) VALUES ("'+this_login+'","'+hash+'","no")'; #log pwd

    this_cursor.execute(sql_code)
    this_connection.commit()

    this_connection.close()

    print("Registered!")

    _=input()
    exit()

usrc_login = input("Type here login")
usrc_password = input("Type here password")
usrc_confirm_password = input("Confirm passwords")

if len(usrc_password) < 8:
    print("Password is too short!")
    _=input()
    exit()
if len(usrc_login) < 8:
    print("Login is too short!")
    _=input()
    exit()
if word_in(usrc_login) != True:
    print("Login contains spaces!")
    _=input()
    exit()
if usrc_password != usrc_confirm_password:
    print("Passwords doesn't match")
    _=input()
    exit()
if usrc_login == "":
    print("Empty login")
    _=input()
    exit()
if usrc_password == "" or usrc_confirm_password == "":
    print("Passwords are empty")
    _=input()
    exit()
if checkuser(usrc_password,connection,cursor) != True:
    print("user exists!")


createuser(usrc_login,usrc_password,connection,cursor)


connection.close()
