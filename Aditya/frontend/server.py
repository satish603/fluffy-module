import PyPDF2
import re
import urllib.request
import json
from flask import Flask, render_template, request,jsonify 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def index1():
    return render_template('signupform.html')


@app.route('/', methods=['POST'])
def getvalue():
    search = request.form['search']
    try:
        from googlesearch import search
    except ImportError: 
        print("No module named 'google' found")
    name = request.form['search']
# to search
    query = name+" filetype:pdf"
    print(query)
    ar = [] 
    for j in search(query, tld="co.in", num=10, stop=3, pause=2):
        ar.append(j)
    return render_template('data.html', s=json.dumps(ar),r=jsonify(ar))


if __name__ == '__main__':
    app.run(debug=True)
