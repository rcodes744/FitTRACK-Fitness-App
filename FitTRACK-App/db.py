import sqlite3
import datetime
def con():

    c = sqlite3.connect('FitTRACK.db')
    cr = c.cursor()
    q1='''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, gender TEXT)'''
    cr.execute(q1)

    q2='''CREATE TABLE IF NOT EXISTS Workouts(wid INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER, date TEXT, exercise TEXT, duration INTEGER, calories_burned INTEGER,
        FOREIGN KEY(userid) REFERENCES users(id))'''
    cr.execute(q2)
    return c

def main():
    c=con()
    print('welcome to FitTRACK')
    print('Main Menu')
    print('1. Register User')
    print('2. log exercise')
    print('3. add exercise')
    print('4. view progress')
    print('5.exit')

    choice=input('enter your choice')
    if choice=='1':
        print('Register User...')
        n=input('enter name: ')
        a=int(input('enter age: '))
        g=input('enter gender: ')
        cr = c.cursor()
        q = 'INSERT INTO users(name,age,gender) VALUES (?,?,?)'
        cr.execute(q,(n,a,g))
        c.commit()
        q2 = 'SELECT id FROM users WHERE name=?'
        rs=cr.execute(q2,(n,)).fetchall()
        id = rs[0][0]
        print(f'user {n}registered successfully! with id')

    elif choice=='2':
        cr=c.cursor()
        uid=int(input('enter user id:'))
        date  =datetime.date.today().strftime('%y-%m-%d')
        execise = input('enter exercise name: ')
        duration = int(input('enter the duration(in minutes):'))
        calories_burned = int(input('enter caleries burned:'))

    elif choice=='4':
        cr= c.cursor()
        q='SELECT * FROM users'
        rs=cr.execute(q).fetchall()
        for row in rs:
            print(f'ID: {row[0]} ,Name: {row[1]}, Age: {row[2]}')
    
        c.close()
main()

if __name__=="__main__":
    #main function
    main()




"""
import sqlite3
import datetime

def con():
    c = sqlite3.connect('FitTRACK.db')
    cr = c.cursor()
    q1 = '''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, gender TEXT)'''
    cr.execute(q1)

    q2 = '''CREATE TABLE IF NOT EXISTS Workouts(wid INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER, date TEXT, exercise TEXT, duration INTEGER, calories_burned INTEGER,
        FOREIGN KEY(userid) REFERENCES users(id))'''
    cr.execute(q2)
    return c

def register_user(c):
    print('Register User...')
    n = input('enter name: ')
    a = int(input('enter age: '))
    g = input('enter gender: ')
    cr = c.cursor()
    q = 'INSERT INTO users(name,age,gender) VALUES (?,?,?)'
    cr.execute(q, (n, a, g))
    c.commit()
    q2 = 'SELECT id FROM users WHERE name=?'
    rs = cr.execute(q2, (n,)).fetchall()
    id_val = rs[0][0]
    print(f'user {n} registered successfully! with id {id_val}')

def log_exercise(c):
    cr = c.cursor()
    uid = int(input('enter user id: '))
    date = datetime.date.today().strftime('%Y-%m-%d')
    exercise = input('enter exercise name: ')
    duration = int(input('enter the duration (in minutes): '))
    calories_burned = int(input('enter calories burned: '))
    q = '''INSERT INTO Workouts(userid, date, exercise, duration, calories_burned)
           VALUES (?, ?, ?, ?, ?)'''
    cr.execute(q, (uid, date, exercise, duration, calories_burned))
    c.commit()
    print('Exercise logged successfully!')

def view_progress(c):
    cr = c.cursor()
    q = 'SELECT * FROM users'
    rs = cr.execute(q).fetchall()
    print('Users:')
    for row in rs:
        print(f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}')
    
    uid = int(input('Enter user ID to view workouts (or 0 to skip): '))
    if uid != 0:
        q2 = '''SELECT date, exercise, duration, calories_burned FROM Workouts 
                WHERE userid=? ORDER BY date DESC'''
        rs2 = cr.execute(q2, (uid,)).fetchall()
        print(f'Workouts for user {uid}:')
        total_cal = sum(row[3] for row in rs2)
        for row in rs2:
            print(f'Date: {row[0]}, Exercise: {row[1]}, Duration: {row[2]} min, Calories: {row[3]}')
        print(f'Total calories burned: {total_cal}')

def main():
    c = con()
    while True:
        print('\nwelcome to FitTRACK')
        print('Main Menu')
        print('1. Register User')
        print('2. Log exercise')
        print('3. Add exercise (not implemented)')
        print('4. View progress')
        print('5. Exit')
        choice = input('enter your choice: ')
        
        if choice == '1':
            register_user(c)
        elif choice == '2':
            log_exercise(c)
        elif choice == '4':
            view_progress(c)
        elif choice == '5':
            c.close()
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()

"""