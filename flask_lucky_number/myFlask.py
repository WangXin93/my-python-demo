from flask import Flask
from flask import render_template
import random

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

if __name__ == "__main__":
    app.run()
