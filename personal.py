import sqlite3

global db
global sql

db = sqlite3.connect('server_personal.db')
sql = db.cursor()

sql.execute(
    """    
    CREATE TABLE IF NOT EXISTS users( 
    login TEXT,
    password TEXT,
    cash INT
 )
   """
)


def reg():
    db.commit()
    user_login = input('Login:')
    user_password = input('Password:')
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
        db.commit()
        print('Registered')
    else:
        print("There is such a record")

    for value in sql.execute("SELECT * FROM users"):
        print(value)


def delete_db():
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}' ")
    db.commit()

    print('The entry has been deleted!')


def casino():
    global user_login
    user_login = input('Login in: ')
    number = 7
    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('This login does not exist')
        reg()
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = '{100}' WHERE login = '{user_login}'")
            db.commit()
        else:
            print('LOSE!')
            delete_db()


def main():
    casino()



main()