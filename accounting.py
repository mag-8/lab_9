import sqlite3

base = sqlite3.connect('db1.db')
cur = base.cursor()

r = cur.execute ('SELECT * FROM income').fetchall()
print(r)

cur.execute('INSERT INTO income VALUES(?,?,?,?)', ('21000', '1200', '100', '5000'))
base.commit()

print("Результат після вставки")
r = cur.execute ('SELECT * FROM income').fetchall()
print(r)

cur.execute('UPDATE income SET salary == ? WHERE salary == ?', ('20000', '12000'))
base.commit()

print("Результат після редагування")
r = cur.execute ('SELECT * FROM income').fetchall()
print(r)

cur.execute('DELETE FROM income WHERE salary == ?', ('20000',))
base.commit()

print("Результат після видалення")
r = cur.execute ('SELECT * FROM income').fetchall()
print(r)