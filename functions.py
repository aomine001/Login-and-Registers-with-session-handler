import sqlite3

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
