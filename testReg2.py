from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'lol_da_ladno_kak_ti_ego_ugadal'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/newsession', methods = ['GET', 'POST'])
def newsession():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return '''
        <form action="" method="POST">
        <p><input type=text name=username>
        <p><input type=submit value=log in>
    '''

@app.route('/delsession', methods = ['GET', 'POST'])
def delsession():
    session.pop('username', None)
    return redirect(url_for('newsession'))


# Views
@app.route('/')
def home():
    if 'username' in session:
        name = session['username']
        return render_template('test.html', username=name)
    else:
        return redirect(url_for('newsession'))
