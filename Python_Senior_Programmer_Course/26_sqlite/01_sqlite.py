import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE users(id INTEGER, name TEXT)")
con.execute("INSERT INTO users VALUES (?, ?)", (1, "Ada"))
for row in con.execute("SELECT * FROM users"): print(row)
con.close()