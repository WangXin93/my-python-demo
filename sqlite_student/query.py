import sqlite3

conn = sqlite3.connect('mytest.db')
cursor = conn.cursor()
sql = "SELECT * FROM students"
results = cursor.execute(sql)
all_students = results.fetchall()
for student in all_students:
    student = map(str, student)
    print(' - '.join(student))
