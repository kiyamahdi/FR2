import sqlite3
from tabulate import tabulate
import os

file = os.getcwd()

class DB:
    def __init__(self):
        conn = sqlite3.connect(f'{file}//FR_DB.db')
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS FACES(id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, age TEXT, gender TEXT)
        """)
        conn.commit()
        conn.close()
    def add(fname, lname, age, gender):
        conn = sqlite3.connect('FR_DB.db')
        c = conn.cursor()
        c.execute("""
        INSERT INTO FACES (fname,lname,age,gender) 
        VALUES(:fname, :lname, :age, :gender)
        """, {'fname':fname,'lname':lname,'age':age,'gender':gender})
        conn.commit()
        conn.close()
    def show(id):
        conn = sqlite3.connect('FR_DB.db')
        c = conn.cursor()
        c.execute("""
        SELECT fname FROM FACES WHERE id = :id
        """, {'id': id})
        fname = tabulate(c.fetchall(), tablefmt="plain")
        c.execute("""
        SELECT lname FROM FACES WHERE id = :id
        """, {'id': id})
        lname = tabulate(c.fetchall(), tablefmt="plain")
        c.execute("""
        SELECT age FROM FACES WHERE id = :id
        """, {'id': id})
        age = tabulate(c.fetchall(), tablefmt="plain")
        c.execute("""
        SELECT gender FROM FACES WHERE id = :id
        """, {'id': id})
        gender = tabulate(c.fetchall(), tablefmt="plain")

        return fname, lname, age, gender

