from requests import get
import sqlite3
import hashlib
import uuid
import os
import time

os.system('cls')

ip = get('https://api.ipify.org').text


def CREATE_SESSION(ip, username):
    this_ip = ip
    this_username = username
    this_uuid = uuid.uuid1()

    SESSION_CONNECTION=sqlite3.connect('SESSION.db')
    SESSION_CURSOR=SESSION_CONNECTION.cursor()

    sql = 'INSERT INTO session (ip,uuid,user) VALUES ("' + this_ip + '","' + str(this_uuid) + '","' + this_username +'");'

    SESSION_CURSOR.execute(sql)
    SESSION_CONNECTION.commit()

    print("Logged in with success!")

    SESSION_CONNECTION.close()
    os.system('python login.py')
    exit()
def logout(ip):
    this_ip = ip

    SESSION_CONNECTION=sqlite3.connect('SESSION.db')
    SESSION_CURSOR=SESSION_CONNECTION.cursor()

    sql = 'DELETE FROM session WHERE ip="' + this_ip + '";'

    SESSION_CURSOR.execute(sql)
    SESSION_CONNECTION.commit()

    print("Logged out.")
    SESSION_CONNECTION.close()

    os.system('python login.py')
    exit()
def CHECK_FOR_SESSION(ip):
    username = ''

    usersdb = sqlite3.connect('users.db')
    userscursor = usersdb.cursor()

    this_ip = ip
    SESSION_CONNECTION=sqlite3.connect('SESSION.db')
    SESSION_CURSOR=SESSION_CONNECTION.cursor()

    sql = 'SELECT * FROM session WHERE ip="' + this_ip + '"'

    SESSION_CURSOR.execute(sql)
    SESSION_CONNECTION.commit()

    rows = SESSION_CURSOR.fetchall()
    try:
        username = rows[0][2]
    except IndexError:
        pass

    sql2 = 'SELECT * FROM users WHERE log="' + username + '"'

    userscursor.execute(sql2)
    usersdb.commit()

    rows2 = userscursor.fetchall()

    try:
        ban = rows2[0][2]
    except:
        pass

    try:
        if ban == "yes":
            print("THIS USER IS BANNED!")
            print("LOGGING OUT THE USER!")
            _=input()
            logout(ip)
            usersdb.close()
            SESSION_CONNECTION.close()
            exit()
    except UnboundLocalError:
        pass

    usersdb.close()

    if len(rows) != 0:
        return False
    else:
        return True

    SESSION_CONNECTION.close()
def login():

    useroption_login = input("Type here login")
    useroption_password = input("Type here password")

    to_hash = str(useroption_password).encode('utf-8')
    hash = hashlib.md5(to_hash).hexdigest()

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    sql = 'SELECT * FROM users WHERE log="'+useroption_login+'" AND pwd="'+hash+'"'
    cursor.execute(sql)
    connection.commit()

    rows = cursor.fetchall()

    length = len(rows)

    if length != 0:
        print('Logging in...')

        if CHECK_FOR_SESSION(ip) == True:
            CREATE_SESSION(ip, useroption_login)
        else:
            os.system('python login.py')
            exit()
    else:
        print("User doesn't exist.")
        time.sleep(3)
        os.system('python login.py')
        exit()

    connection.close()
def check():
    if CHECK_FOR_SESSION(ip) != True:
        print("hello!")
        while True:
            print("-------------")
            print("1.Logout")
            print("2.Exit app")
            print("-------------")
            com = input("Choose action")


            if com == str(1):
                logout(ip)
            elif com == str(2):
                exit()
            else:
                print("Operation not found")
    else:
        login()

check()
