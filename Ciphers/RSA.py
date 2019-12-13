import random
import copy
import sys

alfavit = tuple("abcdefghijklmnopqrstuvwxyz ,.0123456789?*")

def inputTextKey(mode, inputText = '', inputKeys = ''):

    while True:
        err = 0
        if mode == 0:
            if inputText == '':
                text = input("Введите открытый текст: ")
            else:
                text = inputText

            code = list()
            for i in text:
                if i in alfavit:
                    code.append(alfavit.index(i))
                else:
                    print(i, "не находится в алфавите")


        if mode == 1:
            if inputText == '':
                text = input("Введите шифр: ")
            else:
                text = inputText

            try:
                codeT = text.split(' ')
                code = list()
                for i in codeT:
                    if i != '':
                        code.append(int(i))
            except:
                print("шифр должен состоять из цифр не букв, А ЦИФР")
                code = ''
            #print(code)

        if inputKeys == '':
            if mode == 0:
                keyT = input("Введите открытый ключ (g - генерировать автоматически):")
            if mode == 1:
                keyT = input("Введите закрытый ключ:")
        else:
            keyT = inputKeys

        ############## перевод текста в код




        key = list()

        if keyT == 'g':
            e, d, n = generateKey()
            print('Открытый ключ: ', e, n)
            print('Закрытый ключ: ', d, n)
            key.append(e)
            key.append(n)
        else:
            key = keyT.split(' ')
            if len(key) == 2:
                try:
                    key[0] = int(key[0])
                    key[1] = int(key[1])
                except:
                    print("ключ должен состоять из цифр не букв, А ЦИФР")


        if len(code) != 0 and len(key) == 2:
            break
        else:
            if inputText == '' and inputKeys == '':
                return [1,2,3], 1, 10


    #print(code, key, keyMatrix)#
    return code, key[0], key[1]


def outputText(code, consoleOutput = True):
    ############## перевод текста в код
    text = ""
    for i in code:
        if i < len(alfavit):
            text += alfavit[i]
        else:
            print(i, ' - выходит за предел')

    if consoleOutput is True:
        print(text)
    else:
        return text

def outputCode(code, consoleOutput = True):
    ############## перевод текста в код
    text = ""
    for i in code:
        text += str(i) + ' '
    if consoleOutput is True:
        print(text)
    else:
        return text

def createD(m):
    end = False
    while not end:
        d = random.randint(0b0000000011111111, 0b1111111111111111)
        a = d
        b = m
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        #print(a + b)
        if a + b == 1:
            end = True
    return d


def createMOE(a, m):
    x = a
    y = m
    # x = 7
    # y = 11
    z = 1
    steckk = []

    steckk.append(x)
    steckk.append(y)
    steckk.append(z)

    while (x > 1):
        buf = y
        y = x
        x = buf % x
        z = -z
        steckk.append(x)
        steckk.append(y)
        steckk.append(z)

        # print(x, y, z)

    i = 1
    while (len(steckk) >= 3):
        z = steckk.pop()
        y = steckk.pop()
        x = steckk.pop()
        i = (y * i + z) / x
        # if i > m:
        # i = i % m

    if i > m:
        i = i % m
    # print(int(i))
    return int(i)

def generateKey():
    # генерация двух простых чисел
    end = 2
    npc = 0
    primeNumber = list()
    while npc < end:
        n = random.randint(0b0000000011111111, 0b1111111111111111)

        if n % 2 != 0:
            for i in range(3, n+1, 2):
                if i*i-1 > n:
                    print('используется простое число - ', n)
                    primeNumber.append(n)
                    npc += 1
                    break
                if n % i == 0:
                    #print(n, 'составное', i)
                    break
    # Получение ключей
    n = primeNumber[0] * primeNumber[1]
    print('n = ', n)
    m = (primeNumber[0] - 1) * (primeNumber[1] - 1)
    print ('m = ', m)
    d = createD(m)
    print('d = ', d)
    e = createMOE(d, m)
    print('e = ', e)
    if (e * d) % m != 1:
        print((e * d) % m, 'Всё очень плохо!!! Хотя может и нет. В общем, удаче тебе в поиске бага )')
    return e, d, n

def RSA(code, key1, key2):
    cipher = list()
    for i in code:
        cipher.append(pow(i, key1, key2))
    return  cipher

def test():
   code, key1, key2 = inputTextKey(0)
   cipher = RSA(code, key1, key2)
   #print(cipher)
   outputCode(cipher)

   code, key1, key2 = inputTextKey(1)
   cipher = RSA(code, key1, key2)
   #print(cipher)
   outputText(cipher)


def job():
    try:
        while True:
            comand = input("Что делать?  1 - Шифровать  2 - Расшифровывать g - Генерировать ключи  t - Тестировать  q - Выйти:")
            if(comand == '1'):
                code, key1, key2 = inputTextKey(0)
                cipher = RSA(code, key1, key2)
                # print(cipher)
                print('Я сделал: ', end='')
                outputCode(cipher)
            elif(comand == '2'):
                code, key1, key2 = inputTextKey(1)
                cipher = RSA(code, key1, key2)
                # print(cipher)
                print('Я расшифровал: ', end='')
                outputText(cipher)
            elif (comand == 'g'):
                generateKey()
            elif(comand == 't'):
                test()
            elif(comand == 'q'):
                print("Пока")
                return 0
            else:
                print("Неизвестная команда. Давай по новой")
    except:
        print("Упсссс....  Что-то пошло не так")

def main():
    job()
    #test()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
