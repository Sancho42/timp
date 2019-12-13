import random
import sys


def vvodT():
    try:
        a = int(input("Введите a (a < 41): "))
        error = False
    
        if a > 40:
            print("Аларм, a больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу а")
            a = random.randint(1, 40)
            print("Я подумал и выбрал ", a)
            error = True
    
        b = int(input("Введите b (b < 41): "))
        if b > 40 and error == False:
            print("Аларм, b больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу b")
            b = random.randint(1, 40)
            print("Я подумал и выбрал ", b)
        if b > 40 and error == True:
            print("Двойной Аларм, b больше 41!!! Второй раз ошибиться и выбрать число больше 40. Так и быть я ещё раз выберу число за тебя )")
            b = random.randint(1, 40)
            print("Пусть это будет ", b)
    except:
        print("Я ничего не понимаю. Как можно ошибиться при вводе чисел? Ты что ввёл буквы вместо чисел??? Я лучше сам сгенерирую a и b")
        a = random.randint(1, 40)
        b = random.randint(1, 40)
        print("Я подумал и выбрал a =", a,"  b =", b)
    
    
    m = 41
    print(a, b, m)
    string = input("Введите открытый текст: ")
    return a, b, m, string

def vvodSh():
    try:
        a = int(input("Введите a (a < 41): "))
        error = False
    
        if a > 40:
            print("Аларм, a больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу а")
            a = random.randint(1, 40)
            print("Я подумал и выбрал ", a)
            error = True
    
        b = int(input("Введите b (b < 41): "))
        if b > 40 and error == False:
            print("Аларм, b больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу b")
            b = random.randint(1, 40)
            print("Я подумал и выбрал ", b)
        if b > 40 and error == True:
            print("Двойной Аларм, b больше 41!!! Второй раз ошибиться и выбрать число больше 40. Так и быть я ещё раз выберу число за тебя )")
            b = random.randint(1, 40)
            print("Пусть это будет ", b)
    except:
        print("Я ничего не понимаю. Как можно ошибиться при вводе чисел? Ты что ввёл буквы вместо чисел??? Я лучше сам сгенерирую a и b")
        a = random.randint(1, 40)
        b = random.randint(1, 40)
        print("Я подумал и выбрал a =", a,"  b =", b)
    
    
    m = 41
    print(a, b, m)
    string = input("Введите шифротекст: ")
    return a, b, m, string

def vvodTRec():
    try:
        a1 = int(input("Введите a1(a1 < 41): "))
        a2 = int(input("Введите a2(a2 < 41): "))
        error = False
    
        if a1 > 40 or a2 > 40:
            print("Аларм, a больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу а")
            a1 = random.randint(1, 40)
            a2 = random.randint(1, 40)
            print("Я подумал и выбрал ", a1, a2)
            error = True
    
        b1 = int(input("Введите b1 (b1 < 41): "))
        b2 = int(input("Введите b2 (b2 < 41): "))
        if (b1 > 40 or b2 > 40) and error == False:
            print("Аларм, b больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу b")
            b1 = random.randint(1, 40)
            b2 = random.randint(1, 40)
            print("Я подумал и выбрал ", b1, b2)
        if (b1 > 40 or b2 > 40) and error == True:
            print("Двойной Аларм, b больше 41!!! Второй раз ошибиться и выбрать число больше 40. Так и быть я ещё раз выберу число за тебя )")
            b1 = random.randint(1, 40)
            b2 = random.randint(1, 40)
            print("Пусть это будет ", b1, b2)
    except:
        print("Я ничего не понимаю. Как можно ошибиться при вводе чисел? Ты что ввёл буквы вместо чисел??? Я лучше сам сгенерирую a и b")
        a1 = random.randint(1, 40)
        b1 = random.randint(1, 40)
        a2 = random.randint(1, 40)
        b2 = random.randint(1, 40)
        print("Я подумал и выбрал a =", a1, a2,"  b =", b1, b2)
    
    
    m = 41
    print(a1, a2, b1, b2, m)
    string = input("Введите открытый текст: ")
    return a1, a2, b1, b2, m, string

def vvodShRec():
    try:
        a1 = int(input("Введите a1(a1 < 41): "))
        a2 = int(input("Введите a2(a2 < 41): "))
        error = False
    
        if a1 > 40 or a2 > 40:
            print("Аларм, a больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу а")
            a1 = random.randint(1, 40)
            a2 = random.randint(1, 40)
            print("Я подумал и выбрал ", a1, a2)
            error = True
    
        b1 = int(input("Введите b1 (b1 < 41): "))
        b2 = int(input("Введите b2 (b2 < 41): "))
        if (b1 > 40 or b2 > 40) and error == False:
            print("Аларм, b больше 41!!! Тебе ничего нелзя доверить, я лучше сам выберу b")
            b1 = random.randint(1, 40)
            b2 = random.randint(1, 40)
            print("Я подумал и выбрал ", b1, b2)
        if (b1 > 40 or b2 > 40) and error == True:
            print("Двойной Аларм, b больше 41!!! Второй раз ошибиться и выбрать число больше 40. Так и быть я ещё раз выберу число за тебя )")
            b1 = random.randint(1, 40)
            b2 = random.randint(1, 40)
            print("Пусть это будет ", b1, b2)
    except:
        print("Я ничего не понимаю. Как можно ошибиться при вводе чисел? Ты что ввёл буквы вместо чисел??? Я лучше сам сгенерирую a и b")
        a1 = random.randint(1, 40)
        b1 = random.randint(1, 40)
        a2 = random.randint(1, 40)
        b2 = random.randint(1, 40)
        print("Я подумал и выбрал a =", a1, a2,"  b =", b1, b2)
    
    
    m = 41
    print(a1, a2, b1, b2, m)
    string = input("Введите шифротекст: ")
    return a1, a2, b1, b2, m, string

    
def vivod(string):
    print("Я сделаль: ", string)

def inCode (string):
    cod = []
    for i in string:
        if i == " ":
            cod.append(26)
            #print(26, end = ' - ')
            #print(i)
        elif i == ".":
            cod.append(27)
            #print(27, end = ' - ')
            #print(i)
        elif i == ",":
            cod.append(28)
            #print(28, end = ' - ')
            #print(i)
        elif i == "!":
            cod.append(29)
            #print(29, end = ' - ')
            #print(i)
        elif i == "?":
            cod.append(40)
            #print(40, end = ' - ')
            #print(i)
        elif ord(i) >= 97 and ord(i) <= 122:
            cod.append(ord(i) - 97)
            #print(ord(i) - 97, end = ' - ')
            #print(i)
        elif ord(i) >= 48 and ord(i) <= 57:
            cod.append(ord(i) - 18)
            #print(ord(i) - 18, end = ' - ')
            #print(i)
        else:
            print(i, "неизвестный знак и он не попадёт в шифротекст, потому что я так хочу", sep = ' - ')
    return cod

def inText(cod):
    string = ""
    for i in cod:
        if i == 26:
            string += " "
            #print(" ", end = ' - ')
            #print(i)
        elif i == 27:
            string += "."
            #print(".", end = ' - ')
            #print(i)
        elif i == 28:
            string += ","
            #print(",", end = ' - ')
            #print(i)
        elif i == 29:
            string += "!"
            #print("!", end = ' - ')
            #print(i)
        elif i == 40:
            string += "?"
            #print("?", end = ' - ')
            #print(i)
        elif i >= 0 and i <= 25:
            string += chr(int(i + 97))
            #print(chr(int(i + 97)), end = ' - ')
            #print(i)
        elif i >= 30 and i <= 39:
            string += chr(int(i + 18))
            #print(chr(int(i + 18)), end = ' - ')
            #print(i)
        else:
            print(i, "Если ты читаешь этот текст - значит что то пошло не так, но я не скажу что )", sep = ' - ')
    return string

def affineCoding (a, b, m, cod):
    buf = []
    codCopy = cod.copy()
    while(len(codCopy) > 0):
        x = codCopy.pop(0)
        buf.append((x * a + b) % m)
    return buf

def affineDecoding (a, b, m, cod):
    buf = []
    codCopy = cod.copy()
    while(len(codCopy) > 0):
        x = codCopy.pop(0)
        if x < b:
            x = x + m
        buf.append(((x - b) * a) % m)
    return buf 

def affineRecurentCoding (a1, a2, b1, b2, m, cod):
    buf = []
    codCopy = cod.copy()
    
    
    loc = 0
    for i in codCopy:
        #x = codCopy.pop(0)
        if loc == 0:
            za = a1
            zb = b1
        elif loc == 1:
            za = a2
            zb = b2
        else:
            za = a2 * a1
            if za >= m:
                za = za % m
            a1 = a2
            a2 = za
            zb = b2 + b1
            if zb >= m:
                zb = zb % m
            b1 = b2
            b2 = zb
        buf.append((i * za + zb) % m)
        loc += 1
        #print(za, zb)#
    #print(buf)#
    return buf

def affineRecurentDecoding (a1, a2, b1, b2, m, cod):
    buf = []
    codCopy = cod.copy()
    
    
    loc = 0
    for i in codCopy:
        #x = codCopy.pop(0)
        if loc == 0:
            za = a1
            zb = b1
        elif loc == 1:
            za = a2
            zb = b2
        else:
            za = a2 * a1
            if za >= m:
                za = za % m
            a1 = a2
            a2 = za
            zb = b2 + b1
            if zb >= m:
                zb = zb % m
            b1 = b2
            b2 = zb
        nza = createMOE(za, m)

        if i < zb:
            i += m

        buf.append(((i - zb) * nza) % m)
        loc += 1
        #print(za, nza, zb)#
    #print(buf)#
    return buf



def coding (a = 0, b = 0, m = 0, text = " "):
    if a == 0:
        a, b, m, text = vvodT()

    cod = inCode(text)
    cod = affineCoding(a, b, m, cod)
    text = inText(cod)
    return text

def decoding (a = 0, b = 0, m = 0, text = " "):
    if a == 0:
        a, b, m, text = vvodSh()

    cod = inCode(text)
    a = createMOE(a, m)
    cod = affineDecoding(a, b, m, cod)
    text = inText(cod)
    return text

def codingRec (a1 = 0, a2 = 0, b1 = 0, b2 = 0, m = 0, text = " "):
    if a1 == 0:
        a1, a2, b1, b2, m, text = vvodTRec()

    cod = inCode(text)
    #print(cod)
    cod = affineRecurentCoding (a1, a2, b1, b2, m, cod)
    #print(cod)
    text = inText(cod)
    return text

def decodingRec (a1 = 0, a2 = 0, b1 = 0, b2 = 0, m = 0, text = " "):
    if a1 == 0:
        a1, a2, b1, b2, m, text = vvodShRec()

    cod = inCode(text)
    #print(cod)
    cod = affineRecurentDecoding (a1, a2, b1, b2, m, cod)
    #print(cod)
    text = inText(cod)
    return text

def createMOE (a, m):
    x = a
    y = m
    #x = 7
    #y = 11
    z = 1
    steckk = []

    steckk.append(x)
    steckk.append(y)
    steckk.append(z)

    while(x > 1):
        buf = y
        y = x
        x = buf % x
        z = -z
        steckk.append(x)
        steckk.append(y)
        steckk.append(z)
        
        #print(x, y, z)

    i = 1
    while(len(steckk) >= 3):
        z = steckk.pop()
        y = steckk.pop()
        x = steckk.pop()
        i = (y * i + z)/x
        #if i > m:
            #i = i % m

    if i > m:
        i = i % m
    #print(int(i))
    return int(i)

def test():
    print("Провожу проверку Аффинного шифра....")
    print("По порядку алфавита:")
    testList = []

    for i in range(41):
        testList.append(i)

    testText = inText(testList)
    print("Открытый текст: ", testText)
    a = random.randint(1, 40)
    b = random.randint(1, 40)
    m = 41
    print("a =", a, "b =", b, "m =", m)
    testText = coding(a, b, m, testText)
    print("Получившийся шифротекст:", end = " ")
    vivod(testText)
    testText = decoding(a, b, m, testText)
    print("Получившийся текст после расшифровки:", end = " ")
    vivod(testText)

    print("А теперь случайный текст:")
    testList = []

    for i in range(41):
        testList.append(random.randint(0, 40))

    testText = inText(testList)
    print("Открытый текст: ", testText)
    a = random.randint(1, 40)
    b = random.randint(1, 40)
    m = 41
    print("a =", a, "b =", b, "m =", m)
    testText = coding(a, b, m, testText)
    print("Получившийся шифротекст:", end = " ")
    vivod(testText)
    testText = decoding(a, b, m, testText)
    print("Получившийся текст после расшифровки:", end = " ")
    vivod(testText)
    ##################################
    print("Провожу проверку Аффинного рекурентного шифра....")
    print("По порядку алфавита:")
    testList = []

    for i in range(41):
        testList.append(i)

    testText = inText(testList)
    print("Открытый текст: ", testText)
    a1 = random.randint(1, 40)
    a2 = random.randint(1, 40)
    b1 = random.randint(1, 40)
    b2 = random.randint(1, 40)
    m = 41
    print("a1 =", a1, "a2 =", a2, "b1 =", b1, "b2 =", b2, "m =", m)
    testText = codingRec(a1, a2, b1, b2, m, testText)
    print("Получившийся шифротекст:", end = " ")
    vivod(testText)
    testText = decodingRec(a1, a2, b1, b2, m, testText)
    print("Получившийся текст после расшифровки:", end = " ")
    vivod(testText)

    print("А теперь случайный текст:")
    testList = []

    for i in range(41):
        testList.append(random.randint(0, 40))

    testText = inText(testList)
    print("Открытый текст: ", testText)
    a1 = random.randint(1, 40)
    a2 = random.randint(1, 40)
    b1 = random.randint(1, 40)
    b2 = random.randint(1, 40)
    m = 41
    print("a1 =", a1, "a2 =", a2, "b1 =", b1, "b2 =", b2, "m =", m)
    testText = codingRec(a1, a2, b1, b2, m, testText)
    print("Получившийся шифротекст:", end = " ")
    vivod(testText)
    testText = decodingRec(a1, a2, b1, b2, m, testText)
    print("Получившийся текст после расшифровки:", end = " ")
    vivod(testText)

def test2():
    print(createMOE(37, 41))

def main():
    #test2()
    j = 100
    while(j > 0):
        i = input("Что будем делать? 1 - Кодировать 2 - Раскодировать t - Тестировать e - Выходить из программы : ")
        text = "?????????"

        if i == "1":
            i = input("Какой шифр использовать? 1 - Аффинный 2 - Аффинный рекурентный : ")
            if i == "1":
                text = coding()
                j -= random.randint(1, 20)
            elif i == "2":
                text = codingRec()
                j -= random.randint(1, 30)
            else:
                print("неизвестная команда")
                j -= random.randint(1, 40)
            vivod(text)
        elif i == "2":
            i = input("Какой шифр использовать? 1 - Аффинный 2 - Аффинный рекурентный : ")
            if i == "1":
                text = decoding()
                j -= random.randint(1, 20)
            elif i == "2":
                text = decodingRec()
                j -= random.randint(1, 30)
            else:
                print("неизвестная команда")
                j -= random.randint(1, 40)
            vivod(text)
        elif i == "t":
            test()
            j -= random.randint(1, 20)
        elif i == "e":
            input("Ну и уходи")
            return 0
        else:
            print("Сложна! Сложна! Сложна! Ничего не ПАНЯТНА. Давай по новой")
            j -= random.randint(1, 100)

    input("Я устал, уходи")

if __name__ == "__main__":
    sys.exit(int(main() or 0))
