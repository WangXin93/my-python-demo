from flask import Flask
from flask import render_template
import random
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/test/')
def test_page():
    return 'This is a test page.'

@app.route('/lucky/')
def lucky():
    lucky_num = random.randint(1,100)
    return render_template('./lucky.html',
                          lucky_num=lucky_num)

@app.route('/query/')
def query():
    conn = sqlite3.connect('mytest.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM students"
    results = cursor.execute(sql)
    all_students = results.fetchall()
    return render_template('./students.html',
                           all_students=all_students)

if __name__ == "__main__":
    app.run()
