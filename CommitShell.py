import sqlite3
import os

os.system('cls')

def READ(com):
    C = com

    if C[0] == "ban":
        user = C[1]

        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()

        sql = "UPDATE users SET banned = 'yes' WHERE log='" + user + "'"

        cursor.execute(sql)
        connection.commit()

        connection.close()

        print("Banned user: ", user)
    elif C[0] == "unban":
        user = C[1]

        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()

        sql = "UPDATE users SET banned = 'no' WHERE log='" + user + "'"

        cursor.execute(sql)
        connection.commit()

        connection.close()

        print("Unbanned user: ", user)
    elif C[0] == "check-user":
        user = C[1]

        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        sql = 'SELECT * FROM users WHERE log="' + user + '"'

        cursor.execute(sql)
        connection.commit()

        rows = cursor.fetchall()
        print("--------------------------------------")
        print("Username is: ", rows[0][0])
        print("Is user banned? ", rows [0][2])
        print("--------------------------------------")
        
        connection.close()


    elif C[0] == "exit":
        os.system('cls')
        exit()
while True:
    _=input("INT-SHELL=> ")
    commands = _.split()
    READ(commands)
