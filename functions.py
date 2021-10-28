import sqlite3
import uuid
import os
from requests import get

def userexists(user):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    this_user = user

    sql_code = 'SELECT * FROM users WHERE log="' + this_user + '"'

    cursor.execute(sql_code)
    connection.commit()

    rows = cursor.fetchall()

    if len(rows) != 0:
        return True
    else:
        return False
    connection.close()
def getip():
    ip = get('https://api.ipify.org').text
    return ip
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

    os.system('python login.py')
    exit()

    SESSION_CONNECTION.close()
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

    if len(rows) != 0:
        return True
    else:
        return False
