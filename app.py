from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'\xd4\x87\\\x0eJ\x80\x9em=\r\x91d\x9b\xe3c'

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return redirect(url_for('login'))

@app.route('/cabinet')
def cabinet():
    if 'username' in session:
        return render_template('index.html')
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['psw'] = request.form['psw']
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In')

if __name__ == "__main__":
    app.run(debug=True)
