import random
import copy
import sys

alfavit = tuple("abcdefghijklmnopqrstuvwxyz ,.0123456789?*")

def inputTextKey(mode = 0, inputText = '', inputKeys = ''):

    while True:
        err = 0

        if inputText == '':
            if mode == 0:
                text = input("Введите открытый текст: ")
            if mode == 1:
                text = input("Введите шифр: ")
        else:
            text = inputText

        if inputKeys == '':
            keyT = input("Введите ключ :")
        else:
            keyT = inputKeys

        ############## перевод текста в код
        code = list()
        for i in text:
            if i in alfavit:
                code.append(alfavit.index(i))
            else:
                print(i , "не находится в алфавите")

        key = list()
        for i in keyT:
            if i in alfavit:
                key.append(alfavit.index(i))
            else:
                print(i, "не находится в алфавите")
        if len(key) == 0:
            key.append('a')


        if (inputText == '' or inputKeys == '') and len(code) != 0 and len(key) != 0:
            break
        else:
            break

    #print(code, key, keyMatrix)#
    return code, key


def outputText(code, consoleOutput=True):
    ############## перевод текста в код
    text = ""
    for i in code:
        text += alfavit[i]

    if consoleOutput is True:
        print(text)
    else:
        return text

def VigenereCipher(code, key, mod):
    if len(code) > len(key):
        key *= (len(code) // len(key)) + 1
    if mod is True:
        mn = 1
    if mod is False:
        mn = -1

    cipher = list()
    for i, j in enumerate(code):
        cipher.append((j + key[i] * mn) % 41)

    return  cipher

def VigenereCipherHarder(code, key, mod): #Нужно спросить про усланённый шифр!!!!
    if mod is True:
        mn = 1
    if mod is False:
        mn = -1

    keyf = key[0]
    cipher = list()
    for i, j in enumerate(code):
        buf = j
        cipher.append((j + keyf * mn) % 41)
        keyf = buf
        if not mod:
            keyf = cipher[len(cipher) - 1]

    return  cipher


def test():
    code, key = inputTextKey(0)
    cipher = VigenereCipher(code, key, True)
    outputText(cipher)

    code = VigenereCipher(cipher, key, False)
    outputText(code)

    code, key = inputTextKey(0)
    cipher = VigenereCipherHarder(code, key, True)
    outputText(cipher)

    code = VigenereCipherHarder(cipher, key, False)
    outputText(code)

def job():
    #try:
    while True:
        comand = input("Что делать?  1 - Шифровать  2 - Расшифровывать  t - Тестировать  q - Выйти:")
        if(comand == '1'):
            command = input("Какой шифр использовать? 1 - Шифр Виженера  2 - Шифр Виженера с самоключом")
            if command == '1':
                code, key = inputTextKey(0)
                cipher = VigenereCipher(code, key, True)
                outputText(cipher)
            if command == '2':
                code, key = inputTextKey(0)
                cipher = VigenereCipherHarder(code, key, True)
                outputText(cipher)
        elif(comand == '2'):
            command = input("Какой шифр использовать? 1 - Шифр Виженера  2 - Шифр Виженера с самоключом")
            if command == '1':
                code, key = inputTextKey(1)
                cipher = VigenereCipher(code, key, False)
                outputText(cipher)
            if command == '2':
                code, key = inputTextKey(1)
                cipher = VigenereCipherHarder(code, key, False)
                outputText(cipher)
        elif(comand == 't'):
            test()
        elif(comand == 'q'):
            print("Пока")
            return 0
        else:
            print("Неизвестная команда. Давай по новой")
    #except:
        #print("Упсссс....  Что-то пошло не так")

def main():
    job()
    #test()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
