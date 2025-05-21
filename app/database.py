import sqlite3

def init_db():
    conn = sqlite3.connect('names.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS names (name TEXT)''')
    conn.commit()
    conn.close()

def add_name(name):
    conn = sqlite3.connect('names.db')
    c = conn.cursor()
    c.execute("INSERT INTO names VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_names():
    conn = sqlite3.connect('names.db')
    c = conn.cursor()
    c.execute("SELECT * FROM names")
    names = c.fetchall()
    conn.close()
    return names