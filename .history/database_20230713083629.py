import sqlite3
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE pass (username VARCHAR, password VARCHAR, website VARCHAR)')
except:
    print("")

conn.commit()
conn.close()