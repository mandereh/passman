import sqlite3
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE pass (username VARCHAR, password VARCHAR, website VARCHAR)')
except:
    print("")
website = "loveworld.com"
cur.execute("SELECT * FROM pass WHERE website=?",[website])
ans = cur.fetchall()
print(ans)
conn.commit()
conn.close()