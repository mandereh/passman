import sqlite3
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE pass (user VARCHAR, pass VARCHAR, web VARCHAR)')
except:
    print("")

cur.execute("INSERT INTO pass (user,pass,web) VALUES ('Daerego Braide','4332242Ic','nineteen')")
web = "facebook"
cur.execute("SELECT * FROM pass WHERE web=?",[web])
ans = cur.fetchall()
print(ans)
conn.commit()
conn.close()