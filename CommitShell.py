import sqlite3
import os
import functions
import functions

os.system('cls')

def useroutput():
    temponary=input("INT-SHELL=> ")
    C = temponary.split()
    try:
        if C[0] == "ban":

            try:
                user = C[1]
            except IndexError:
                print("Missing arguments, missing argument: user")
                useroutput()

            if functions.userexists(user) != True:
                print("This user doesn't exists!")
                useroutput()

            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()

            sql = "UPDATE users SET banned = 'yes' WHERE log='" + user + "'"

            cursor.execute(sql)
            connection.commit()

            connection.close()

            print("Banned user: ", user)

            useroutput()
        elif C[0] == "unban":
            try:
                user = C[1]
            except IndexError:
                print("Missing arguments, missing argument: user")
                useroutput()

            if functions.userexists(user) != True:
                print("This user doesn't exists!")
                useroutput()

            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()

            sql = "UPDATE users SET banned = 'no' WHERE log='" + user + "'"

            cursor.execute(sql)
            connection.commit()

            connection.close()

            print("Unbanned user: ", user)
        elif C[0] == "checkuser":
            try:
                user = C[1]
            except IndexError:
                print("Missing arguments, missing argument: user")
                useroutput()

            if functions.userexists(user) != True:
                print("This user doesn't exists!")
                useroutput()

            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            sql = 'SELECT * FROM users WHERE log="' + user + '"'

            cursor.execute(sql)
            connection.commit()

            rows = cursor.fetchall()
            print("--------------------------------------")
            print("User ban status:", rows [0][2])
            print("--------------------------------------")

            connection.close()

            useroutput()
        elif C[0] == "exit":
            os.system('cls')
            exit()
        else:
            print("Command not found")
    except IndexError:
        print("You typed nothing")
while True:
    useroutput()
