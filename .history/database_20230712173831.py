import sqlite3
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()

try:
    