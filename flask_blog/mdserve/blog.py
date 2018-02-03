from flask import Flask
import markdown
import os
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<doc>.html")
def mdfile(doc):
    content = open(os.path.join('docs',doc) + '.md').read()
    body = markdown.markdown(content)
    return render_template('layout.html',
                           body=body,
                           doc=doc) 

@app.route("/edit/<doc>.html", methods=['POST','GET'])
def edit(doc):
    if request.method == 'POST':
        contents = request.form['contents']
        with open(os.path.join('docs', doc) + ".md", 'w') as f:
            f.write(contents)
        return redirect(doc + '.html')
    else:
        contents = open(os.path.join('docs', doc) + ".md").read()
        return render_template('edit.html',
                               doc=doc,
                               contents=contents) 

