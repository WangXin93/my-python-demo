import sqlite3

conn = sqlite3.connect('mytest.db')
cursor = conn.cursor()

print("Let's input some students!")
while True:
    name = input("Student's name: ")
    username = input("Student's username: ")
    id_num = input("Student's id number: ")
    sql = '''insert into students
            (name, username, id)
            values
            (:st_name, :st_username, :id_num)'''
    cursor.execute(sql, {'st_name':name, 'st_username':username, 'id_num':id_num})
    conn.commit()
    cont = input("Another student? ([y]/n)") or 'y'
    if cont[0].lower() == 'n':
        break
cursor.close()
conn.close()



