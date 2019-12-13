import sys
import hashlib

import  main as app

def testServerBD():
    print('Тест подсистем сервера, авторизации, регистрации - НАЧАТ')
    process = 0
    try:
        name = 'TEST1234567890TESTname'
        password = 'TEST1234567890TESTpassword'
        newUser = app.User(username=name, password=hashlib.md5(password.encode('utf-8')).hexdigest())
        app.db.session.add(newUser)
        app.db.session.commit()
        process = 1
        print('Создание пользователя - ОК')
    except:
        print('Ошибка при создании пользователя')

    if process == 1:
        try:
            checkUser = app.User.query.filter_by(username=name).first()
            newCipher = app.UsedCipher(inputText='TESTinput',
                                    inputKeys='TESTkeys',
                                    outputText='TESToutput',
                                    encryptionMode='TESTmode', users=checkUser)
            app.db.session.add(newCipher)
            app.db.session.commit()
            process = 2
            print('Создание истории паролей - ОК')
        except:
            print('Ошибка при создании истории шифров')

    if process == 2:
        try:
            history = app.UsedCipher.query.filter_by(id=newCipher.id).first()
            app.db.session.delete(history)
            app.db.session.commit()
            process = 3
            print('Удаление истории паролей - ОК')
        except:
            print('Ошибка при удалении истории шифров')

    if process == 3:
        try:
            checkUser = app.User.query.filter_by(username=name).first()
            process = 4
            print('Авторизация - ОК')
        except:
            print('Ошибка при авторизации')

    if process == 4:
        try:
            checkUser = app.User.query.filter_by(username=name).first()
            app.db.session.delete(checkUser)
            app.db.session.commit()
            process = 5
            print('Удаление пользователя - ОК')
        except:
            print('Ошибка при удалении пользователя')

    if process == 5:
        print('Тест подсистем сервера, авторизации, регистрации - ПРОЙДЕН')

def testCipherSystem():
    print('Тест подсистемы шифрования - НАЧАТ')
    process = 0
    try:
        inputText = 'abcdefghijklmnopqrstuvwxyz ,.0123456789?*'
        keysText = 'key example'
        encryptionMode = 'encryption'
        checkOutputText = 'kf 0i.gtxuovq8*t?r152z3,hk1j.aeb7c9svau?l'
        outputText = app.cipherApp.VigenereCipher(inputText, keysText, encryptionMode)
        if outputText == checkOutputText:
            print('Шифр Виженера - ОК')
            process += 1
    except:
        print('Ошибка в шифре Виженера')

    try:
        inputText = 'abcdefghijklmnopqrstuvwxyz ,.0123456789?'
        keysText = '5 23'
        encryptionMode = 'encryption'
        checkOutputText = 'x,38chmrw.27bglqv 16afkpuz0?5joty!49dins'
        outputText = app.cipherApp.affinityEncryption(inputText, keysText, encryptionMode)
        if outputText == checkOutputText:
            print('Аффинный шифр - ОК')
            process += 1
    except:
        print('Ошибка в Аффинном шифре')

    try:
        inputText = 'abcdefghijklmno123'
        keysText = 'qwertyuio'
        encryptionMode = 'encryption'
        checkOutputText = '1 74b?7rb?4ebihtwz'
        outputText = app.cipherApp.HillEncryption(inputText, keysText, encryptionMode)
        if outputText == checkOutputText:
            print('Шифр Хилла - ОК')
            process += 1
    except:
        print('Ошибка в шифре Хилла')

    try:
        inputText = 'abcdefghijklmnopqrstuvwxyz ,.0123456789?'
        keysText = '11 77'
        encryptionMode = 'encryption'
        checkOutputText = '0 1 46 47 37 38 6 7 8 53 54 44 45 13 14 15 60 61 51 52 20 21 22 67 68 58 59 27 28 29 74 75 65 66 34 35 36 4 5 72 '
        outputText = app.cipherApp.RSA(inputText, keysText, encryptionMode)
        if outputText == checkOutputText:
            print('Шифре RSA - ОК')
            process += 1
    except:
        print('Ошибка в шифре RSA')

    if 0 < process < 4:
        print('Тест подсистемы шифрования - ЧАСТИЧНО ПРОЙДЕН ( пройдено', process, 'тестов шифров)')

    if process == 4:
        print('Тест подсистемы шифрования - ПОЛНОСТЬЮ ПРОЙДЕН')

def main():
    testServerBD()
    testCipherSystem()
    c = input('Enter чтобы закрыть')

if __name__ == "__main__":
    sys.exit(int(main() or 0))