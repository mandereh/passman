import sqlite3
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE pass (username VARCHAR, password VARCHAR, website VARCHAR)')
except:
    print("")
cur.execute("ALTER TABLE pass RENAME COLUMN user TO username")
cur.execute("ALTER TABLE pass RENAME COLUMN pass TO password")
cur.execute("ALTER TABLE pass RENAME COLUMN web TO website")
# web = "nineteen"
# cur.execute("SELECT * FROM pass WHERE web=?",[web])
# ans = cur.fetchall()
# print(ans)
conn.commit()
conn.close()