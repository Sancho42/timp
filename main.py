from collections import namedtuple
import hashlib
import sys

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy

#from dbApp import db
#from dbApp import User
#from dbApp import UsedCipher
#import dbApp#

import cipherApp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:qwe@localhost/dbTiMP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

############################################  ЭТО ДОЛЖНО БЫТЬ ТУТ, ЕСЛИ БРАТЬ ИЗ dbApp всё идёт не так
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1024), nullable=False)
    password = db.Column(db.String(1024), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class UsedCipher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inputText = db.Column(db.String(4096), nullable=False)
    inputKeys = db.Column(db.String(4096), nullable=False)
    outputText = db.Column(db.String(4096), nullable=False)
    encryptionMode = db.Column(db.String(64), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    users = db.relationship('User', backref=db.backref('ciphers', lazy=True))

    def __repr__(self):
        return '<UsedCipher %r>' % self.id
###################################################### ^^^^^^^^^^^^^^^^^^^^^^^^

registrationError = 0

@app.route('/', methods=['GET'])
def startPage():
    print("main-->")
    return render_template('index.html')

@app.route('/main/<username>', methods=['GET', 'POST'])
def main(username):
    print(username)
    #text = request.form['text'] # можно использовать их для передачи имени
    #if request.method == 'POST':
        #username2 = request.form['name']

    checkUser = None
    checkUser = User.query.filter_by(username=username).first()
    # Возможна ошибка если у юзера нет истории
    return render_template('main.html', OUTusedCiphers=reversed(checkUser.ciphers), username=username)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
        if name != '' and password != '' and len(name) < 1024 and len(password) < 1024:  # защита от дурака
            checkUser = None
            checkUser = User.query.filter_by(username=name).first()
            if checkUser is not None:
                if checkUser.password == hashlib.md5(password.encode('utf-8')).hexdigest():
                    return redirect(url_for('main', username=checkUser.username))
            print("check_user-->Не верный логин или пароль")
            return render_template('login.html', massage='Не верный логин или пароль!')
    return render_template('login.html', massage='Введите логин и пароль')


@app.route('/registration', methods=['GET'])
def registration():
    global registrationError
    if registrationError == 0:
        return render_template('registration.html', massage='')
    elif registrationError == 1: # Такой пользователь уже есть
        registrationError = 0
        return render_template('registration.html', massage='Такой пользователь уже есть!')

@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    name = request.form['name']
    password = request.form['pass']
    #проверка в БД
    if name != '' and password != ''and len(name) < 1024 and len(password) < 1024:  # защита от дурака
        checkUser = None
        checkUser = User.query.filter_by(username=name).first()
        if checkUser is not None:
            print("add_user-->такой пользователь уже есть")
            global registrationError
            registrationError = 1
            return redirect(url_for('registration'))
        #если пользователь новый
        newUser = User(username=name, password=hashlib.md5(password.encode('utf-8')).hexdigest())
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('login'))
    return redirect(url_for('registration'))



@app.route('/cipher', methods=['GET'])
def cipher():
    #cipher_VigenereCipher()
    #return cipher_VigenereCipher()
    return redirect(url_for('cipher_VigenereCipher'))
    #return render_template('cipher.html')

@app.route('/encryption', methods=['POST'])
def encryption():
    pass

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

@app.route('/remove', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        id1 = request.form['IDCipher']
        print(id1)
        history = None
        history = UsedCipher.query.filter_by(id=id1).first()

        usid = history.users
        user = User.query.filter_by(id=usid.id).first()

        db.session.delete(history)
        db.session.commit()

    return redirect(url_for('main', username=user.username))


# блоки шифрования

@app.route('/cipher/VigenereCipher/<moodCipher>', methods=['GET', 'POST'])
def cipher_VigenereCipher(moodCipher):
    inputText = 'abcdefghijklmnopqrstuvwxyz ,.0123456789?*'
    keysText = 'key example'
    outputText = ''

    if request.method == 'POST':
        inputText = request.form['INtext']
        keysText = request.form['INkeys']
        encryptionMode = request.form['encryptionMode']
        outputText = cipherApp.VigenereCipher(inputText, keysText, encryptionMode)
        ##
        checkUser = None
        checkUser = User.query.filter_by(username=moodCipher).first()
        if checkUser is not None and len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                and len(outputText) < 64:
            p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                           encryptionMode='Шифр Виженера'+'-'+inRus(encryptionMode), users=checkUser)
            db.session.add(checkUser)
            db.session.commit()

    return render_template('cipherTemplates/VigenereCipher.html', textqwe=moodCipher,
                           INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText)

@app.route('/cipher/affinityEncryption/<moodCipher>', methods=['GET', 'POST'])
def cipher_affinityEncryption(moodCipher):
    inputText = 'abcdefghijklmnopqrstuvwxyz ,.0123456789?'
    keysText = '5 23'
    outputText = ''

    if request.method == 'POST':
        inputText = request.form['INtext']
        keysText = request.form['INkeys']
        encryptionMode = request.form['encryptionMode']
        outputText = cipherApp.affinityEncryption(inputText, keysText, encryptionMode)
        ##
        checkUser = None
        checkUser = User.query.filter_by(username=moodCipher).first()
        if checkUser is not None and len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                and len(outputText) < 64:
            p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                           encryptionMode='affinityEncryption'+'-'+inRus(encryptionMode), users=checkUser)
            db.session.add(checkUser)
            db.session.commit()

    return render_template('cipherTemplates/affinityEncryption.html', textqwe=moodCipher,
                           INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText)

@app.route('/cipher/HillEncryption/<moodCipher>', methods=['GET', 'POST'])
def cipher_HillEncryption(moodCipher):
    inputText = 'abcdefghijklmno123'
    keysText = 'qwertyuio'
    outputText = ''

    if request.method == 'POST':
        inputText = request.form['INtext']
        keysText = request.form['INkeys']
        encryptionMode = request.form['encryptionMode']
        outputText = cipherApp.HillEncryption(inputText, keysText, encryptionMode)
        ##
        checkUser = None
        checkUser = User.query.filter_by(username=moodCipher).first()
        if checkUser is not None and len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                and len(outputText) < 64:
            p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                           encryptionMode='HillEncryption'+'-'+inRus(encryptionMode), users=checkUser)
            db.session.add(checkUser)
            db.session.commit()

    return render_template('cipherTemplates/HillEncryption.html', textqwe=moodCipher,
                           INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText)

@app.route('/cipher/RSA/<moodCipher>', methods=['GET', 'POST'])
def cipher_RSA(moodCipher):
    inputText = 'abcdefghijklmnopqrstuvwxyz ,.0123456789?'
    keysText = '11 77'
    outputText = ''

    if request.method == 'POST':
        inputText = request.form['INtext']
        keysText = request.form['INkeys']
        encryptionMode = request.form['encryptionMode']
        outputText = cipherApp.RSA(inputText, keysText, encryptionMode)
        ##
        checkUser = None
        checkUser = User.query.filter_by(username=moodCipher).first()
        if checkUser is not None and len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                and len(outputText) < 64:
            p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                           encryptionMode='RSA'+'-'+inRus(encryptionMode), users=checkUser)
            db.session.add(checkUser)
            db.session.commit()

    return render_template('cipherTemplates/RSA.html', textqwe=moodCipher,
                           INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText)

# мусорные функции

def inRus(encryptionMode):
    if encryptionMode == 'encryption':
        return 'шифрование'
    if encryptionMode == 'decryption':
        return 'расшифрование'
