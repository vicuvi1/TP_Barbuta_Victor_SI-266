import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE u(nume, parola)")
db.execute("INSERT INTO u VALUES ('ana', 'x')")

rau = "' OR '1'='1"

q = "SELECT * FROM u WHERE nume = ?"
print("parametrizat:", db.execute(q, (rau,)).fetchall())
