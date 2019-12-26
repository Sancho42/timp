from collections import namedtuple
import hashlib
import sys
import random
import rsa

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import session
from flask_sqlalchemy import SQLAlchemy

#from dbApp import db
#from dbApp import User
#from dbApp import UsedCipher
#import dbApp#

import cipherApp

app = Flask(__name__)

app.secret_key = 'lol_da_ladno_kak_ti_ego_ugadal'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:qwe@localhost/dbTiMP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['DEBUG'] = False
#app.debug = True
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
    inputText = db.Column(db.String(90000), nullable=False)
    inputKeys = db.Column(db.String(4096), nullable=False)
    outputText = db.Column(db.String(90000), nullable=False)
    encryptionMode = db.Column(db.String(64), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    users = db.relationship('User', backref=db.backref('ciphers', lazy=True))

    def __repr__(self):
        return '<UsedCipher %r>' % self.id
###################################################### ^^^^^^^^^^^^^^^^^^^^^^^^

registrationError = 0

@app.route('/newsession', methods = ['GET', 'POST'])
def newSession():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('main'))
    return '''
        <form action="" method="POST">
        <p><input type=text name=username>
        <p><input type=submit value=log in>
    '''

@app.route('/', methods=['GET'])
def startPage():
    return render_template('index.html')

@app.route('/main/<username>', methods=['GET', 'POST'])
def main(username):
    if 'username' in session and session['username'] == username:  # проверка безопасности
        #print(username)
        #text = request.form['text'] # можно использовать их для передачи имени
        #if request.method == 'POST':
            #username2 = request.form['name']

        checkUser = None
        checkUser = User.query.filter_by(username=username).first()
        # Возможна ошибка если у юзера нет истории
        return render_template('main.html', OUTusedCiphers=reversed(checkUser.ciphers), username=username)
    return redirect(url_for('login'))



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
                    session['username'] = request.form['name']
                    return redirect(url_for('main', username=checkUser.username))
            #print("check_user-->Не верный логин или пароль")
            return render_template('login.html', massage='Не верный логин или пароль!')
    return render_template('login.html', massage='Введите логин и пароль')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
        if name != '' and password != '' and len(name) < 1024 and len(password) < 1024:  # защита от дурака
            checkUser = None
            checkUser = User.query.filter_by(username=name).first()
            if checkUser is not None:
                return render_template('registration.html', massage='Такой пользователь уже есть!')
            newUser = User(username=name, password=hashlib.md5(password.encode('utf-8')).hexdigest())
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('registration.html', massage='Придумай логин и пароль')


@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

@app.route('/remove/<moodCipher>', methods=['GET', 'POST'])
def remove(moodCipher):
    if 'username' in session and session['username'] == moodCipher:  # проверка безопасности
        if request.method == 'POST':
            id1 = request.form['IDCipher']
            #print(id1)
            id1 = onlyNumbersWithOutSpace(id1)
            if id1 != '' and len(id1) < 10:
                history = None
                history = UsedCipher.query.filter_by(id=id1).first()
                if history != None:
                    usid = history.users
                    user = User.query.filter_by(id=usid.id).first()

                    if user.username != moodCipher: # чтобы нельзя было удалить чужое
                        return redirect(url_for('main', username=moodCipher))

                    db.session.delete(history)
                    db.session.commit()

        return redirect(url_for('main', username=moodCipher))
    return redirect(url_for('login'))


# блоки шифрования

@app.route('/cipher/VigenereCipher/<moodCipher>', methods=['GET', 'POST'])
def cipher_VigenereCipher(moodCipher):
    if 'username' in session and session['username'] == moodCipher:  # проверка безопасности
        inputText = '' # 'abcdefghijklmnopqrstuvwxyz ,.0123456789?*'
        keysText = ''
        for i in range(random.randint(5, 20)):
            keysText += numbersInAlfavit(random.randint(1, 40))
        outputText = ''

        if request.method == 'POST':
            inputText = request.form['INtext']
            keysText = request.form['INkeys']
            encryptionMode = request.form['encryptionMode']
            inputText = delSpecSimvols(inputText) # чистим от спецсимволов
            keysText = delSpecSimvols(keysText)
            if len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                    and len(encryptionMode) < 64:
                outputText = cipherApp.VigenereCipher(inputText, keysText, encryptionMode)
            ##
            checkUser = None
            checkUser = User.query.filter_by(username=moodCipher).first()
            if checkUser is not None and len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                    and len(encryptionMode) < 64:
                p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                               encryptionMode='Шифр Виженера'+'-'+inRus(encryptionMode), users=checkUser)
                db.session.add(checkUser)
                db.session.commit()

        return render_template('cipherTemplates/VigenereCipher.html', textqwe=moodCipher,
                               INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText)
    return redirect(url_for('login'))

@app.route('/cipher/affinityEncryption/<moodCipher>', methods=['GET', 'POST'])
def cipher_affinityEncryption(moodCipher):
    if 'username' in session and session['username'] == moodCipher:  # проверка безопасности
        inputText = '' # 'abcdefghijklmnopqrstuvwxyz ,.0123456789?'
        keysText = str(random.randint(2, 40)) + ' ' + str(random.randint(2, 40))
        outputText = ''

        if request.method == 'POST':
            inputText = request.form['INtext']
            keysText = request.form['INkeys']
            encryptionMode = request.form['encryptionMode']
            inputText = delSpecSimvols(inputText)  # чистим от спецсимволов
            keysText = onlyNumbers(keysText)
            keysText = onlyFirsTwo(keysText)
            if len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096 \
                    and len(encryptionMode) < 64:
                outputText = cipherApp.affinityEncryption(inputText, keysText, encryptionMode)
            ##
            checkUser = None
            checkUser = User.query.filter_by(username=moodCipher).first()
            if checkUser is not None and len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                    and len(encryptionMode) < 64:
                p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                               encryptionMode='Аффинный шифр'+'-'+inRus(encryptionMode), users=checkUser)
                db.session.add(checkUser)
                db.session.commit()

        return render_template('cipherTemplates/affinityEncryption.html', textqwe=moodCipher,
                               INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText)
    return redirect(url_for('login'))

@app.route('/cipher/HillEncryption/<moodCipher>', methods=['GET', 'POST'])
def cipher_HillEncryption(moodCipher):
    if 'username' in session and session['username'] == moodCipher:  # проверка безопасности
        inputText = 'abcdefghijklmno123'
        keysText = 'qwertyuio'
        outputText = ''

        if request.method == 'POST':
            inputText = request.form['INtext']
            keysText = request.form['INkeys']
            encryptionMode = request.form['encryptionMode']
            inputText = delSpecSimvols(inputText)  # чистим от спецсимволов
            keysText = delSpecSimvols(keysText)
            outputText = cipherApp.HillEncryption(inputText, keysText, encryptionMode)
            ##
            checkUser = None
            checkUser = User.query.filter_by(username=moodCipher).first()
            if checkUser is not None and len(inputText) < 4096 and len(keysText) < 4096 and len(outputText) < 4096\
                    and len(encryptionMode) < 64:
                p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                               encryptionMode='Шифр Хилла'+'-'+inRus(encryptionMode), users=checkUser)
                db.session.add(checkUser)
                db.session.commit()

        return render_template('cipherTemplates/HillEncryption.html', textqwe=moodCipher,
                               INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText)
    return redirect(url_for('login'))

@app.route('/cipher/RSA/<moodCipher>', methods=['GET', 'POST'])
def cipher_RSA(moodCipher):
    if 'username' in session and session['username'] == moodCipher:  # проверка безопасности
        inputText = '' #'abcdefghijklmnopqrstuvwxyz ,.0123456789?'
        keysText = '' #'11 77'
        outputText = ''

        outputPubkey = ''
        outputPrivkey = ''

        if request.method == 'POST':
            inputText = request.form['INtext']
            keysText = request.form['INkeys']
            encryptionMode = request.form['encryptionMode']
            outputPubkey = request.form['OUTpub']
            outputPrivkey = request.form['OUTpriv']
            inputText = delSpecSimvols(inputText)  # чистим от спецсимволов
            keysText = onlyNumbers(keysText)
            keysText = onlyFirsTwo(keysText)
            if encryptionMode == 'decryption':
                inputText = onlyNumbers(inputText)
            if len(inputText) < 89999 and len(keysText) < 89999 and len(outputText) < 89999 \
                    and len(encryptionMode) < 64:
                outputText = cipherApp.RSA(inputText, keysText, encryptionMode)
            ##
            checkUser = None
            checkUser = User.query.filter_by(username=moodCipher).first()
            if checkUser is not None and len(inputText) < 90000 and len(keysText) < 4096 and len(outputText) < 90000\
                    and len(encryptionMode) < 64:
                p = UsedCipher(inputText=inputText, inputKeys=keysText, outputText=outputText,
                               encryptionMode='RSA'+'-'+inRus(encryptionMode), users=checkUser)
                db.session.add(checkUser)
                db.session.commit()

        if outputPubkey == '' and outputPrivkey == '':
            pubkey, privkey = rsa.newkeys(1024)   # rsa генерация ключей
            outputPubkey = str(pubkey['e']) + ' ' + str(pubkey['n'])
            outputPrivkey = str(privkey['d']) + ' ' + str(privkey['n'])

        return render_template('cipherTemplates/RSA.html', textqwe=moodCipher,
                               INtextValues=inputText, INkeysValues=keysText, OUTencryptiontextValues=outputText,
                               OUTpubkey=outputPubkey, OUTprivkey=outputPrivkey)
    return redirect(url_for('login'))

@app.route('/cipher/RSA_createKey/<moodCipher>', methods=['GET', 'POST'])
def cipher_RSA_createKey(moodCipher): ############################################# ВСЁ ДОЛЖНО БЫТЬ В ОДНОЙ ФОРМЕ !!!
    if 'username' in session and session['username'] == moodCipher:  # проверка безопасности
        return redirect(url_for('login'))



# обрабатывающие функции

def inRus(encryptionMode):
    if encryptionMode == 'encryption':
        return 'шифрование'
    if encryptionMode == 'decryption':
        return 'расшифрование'

def delSpecSimvols(inputS):
    clearInputText = ''
    for i in inputS:
        if i != '\n' and i != '\r' and i != '\t' and i != '\v':
            if i in 'abcdefghijklmnopqrstuvwxyz ,.0123456789?*':
                clearInputText = clearInputText + i
    return clearInputText

def onlyNumbers(inputS):
    clearInputText = ''
    for i in inputS:
        if i != '\n' and i != '\r' and i != '\t' and i != '\v':
            if i in ' 0123456789':
                clearInputText = clearInputText + i
    return clearInputText

def onlyNumbersWithOutSpace(inputS):
    clearInputText = ''
    for i in inputS:
        if i != '\n' and i != '\r' and i != '\t' and i != '\v':
            if i in '0123456789':
                clearInputText = clearInputText + i
    return clearInputText

def onlyFirsTwo(inputS:str):
    clearInputText = ''
    inputS = inputS.strip()
    buf = inputS.split(' ')
    buf2 = []
    for i in buf:
        if i != '':
            buf2.append(i)
    if len(buf2) > 1:
        clearInputText = buf2[0] + ' ' + buf2[1]
        return clearInputText
    return ''

def numbersInAlfavit(num:int):
    string = 'abcdefghijklmnopqrstuvwxyz, .0123456789? *'
    if 0 < num < 41:
        return string[num]
    return str(num)
