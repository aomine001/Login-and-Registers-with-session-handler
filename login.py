import sqlite3
import hashlib
import os
import time
import functions

os.system('cls')

ip = functions.getip()


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

        if functions.CHECK_FOR_SESSION(ip) != True:

            functions.CREATE_SESSION(ip, useroption_login)
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
    if functions.CHECK_FOR_SESSION(ip) != False:
        print("hello!")
        while True:
            print("-------------")
            print("1.Logout")
            print("2.Exit app")
            print("-------------")
            com = input("Choose action")


            if com == str(1):
                functions.logout(ip)
            elif com == str(2):
                exit()
            else:
                print("Operation not found")
    else:
        login()

check()
