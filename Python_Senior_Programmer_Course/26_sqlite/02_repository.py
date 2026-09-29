import sqlite3
class UserRepository:
    def __init__(self, con): self.con=con
    def add(self, user_id, name):
        self.con.execute("INSERT INTO users VALUES (?,?)",(user_id,name)); self.con.commit()
    def find_all(self): return self.con.execute("SELECT * FROM users").fetchall()
con=sqlite3.connect(":memory:"); con.execute("CREATE TABLE users(id INTEGER,name TEXT)")
r=UserRepository(con); r.add(1,"Ada"); print(r.find_all())