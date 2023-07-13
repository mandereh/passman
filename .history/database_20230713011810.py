import sqlite3
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE pass (user VARCHAR, pass VARCHAR, web VARCHAR)')
except:
    print("")
cur.execute("ALTER TABLE pass RENAME")
web = "nineteen"
cur.execute("SELECT * FROM pass WHERE web=?",[web])
ans = cur.fetchall()
print(ans)
conn.commit()
conn.close()