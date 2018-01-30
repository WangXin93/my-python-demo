import sqlite3

conn = sqlite3.connect('mytest.db')
cursor = conn.cursor()
sql = "select * from students"
results = cursor.execute(sql)
all_students = results.fetchall()
for student in all_students:
    print(student)
