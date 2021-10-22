from flask import Flask, render_template, request


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
    return render_template('data.html', s=search)


if __name__ == '__main__':
    app.run(debug=True)
