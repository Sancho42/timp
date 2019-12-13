import random
import copy
import sys

alfavit = tuple("abcdefghijklmnopqrstuvwxyz ,.0123456789?*")
matrixSize = 3
KeySize = matrixSize * matrixSize

def inputKeyText(mode, rec = 0, inputText = '', inputKeys = ''):

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
            if(rec == 1):
                key = input("Введите ключ (18 символов): ")
            else:
                key = input("Введите ключ (9 символов): ")
        else:
            key = inputKeys
        

        ############## перевод текста в код
        code = list()
        for i in text:
            if i in alfavit:
                code.append(alfavit.index(i))
            else:
                print(i , "не находится в алфавите")

        while len(code) % 3 != 0:
            code.append(40)

        ############# перевод ключа
        if(rec == 0):
            keyMatrix = [[0] * 3 for i in range(3)]
            for j in range(3):
                for i in range(3):
                    if key[j*3 + i] in alfavit:
                        keyMatrix[j][i] = alfavit.index(key[j*3 + i])
                    else:
                        print(key[j*3 + i] , "не находится в алфавите, ключ невалидный")
                        err = 1
                        continue

        ############# перевод ключа при rec = 1
        keyMatrix1 = list()
        if(rec == 1):
            keyMatrix = [[0] * 3 for i in range(3)]
            keyMatrix1 = list()
            for q in range(2):
                for j in range(3):
                    for i in range(3):
                        if key[j*3 + i] in alfavit:
                            keyMatrix[j][i] = alfavit.index(key[q*9 + j*3 + i])
                        else:
                            print(key[q*9 + j*3 + i] , "не находится в алфавите, ключ невалидный")
                            err = 1
                            continue
                if(q == 0):
                    keyMatrix1 = copy.deepcopy(keyMatrix)

        if checkError(key, text, keyMatrix1, keyMatrix) == 0 and err == 0:
            break
        if inputText != '':
            return 12345, [1, 0, 0, 0, 1, 0, 0, 0, 1]

    #print(code, key, keyMatrix)#
    if(rec == 0):
        return code, keyMatrix
    if(rec == 1):
        return code, keyMatrix1, keyMatrix


def outputText(code, consoleOutput=True):
    ############## перевод текста в код
    text = ""
    for i in code:
        if(alfavit[i] != '*'):
            text += alfavit[i]
    if consoleOutput is True:
        print(text)
    else:
        return text

def createMOE (a, m):
    
    a = a % m
    
    x = a
    y = m
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
    #print(int(i))#
    return int(i)

def detMatrix(matrix):
    det = matrix[0][0]*matrix[1][1]*matrix[2][2]+\
        matrix[1][0]*matrix[2][1]*matrix[0][2]+\
        matrix[0][1]*matrix[1][2]*matrix[2][0]-\
        matrix[0][2]*matrix[1][1]*matrix[2][0]-\
        matrix[0][1]*matrix[1][0]*matrix[2][2]-\
        matrix[0][0]*matrix[1][2]*matrix[2][1]
    #print(det)#
    return det


def checkError(key, text, keyMatrix1, keyMatrix2):
    
    if(len(keyMatrix1) == 0):
        if len(key) != 9:
            print("Длина ключа не равна 9")
            return 11
        if detMatrix(keyMatrix2) == 0:
            print("Определитель матрицы равен 0")
            return 21
    else:
        if len(key) != 18:
            print("Длина ключа не равна 18")
            return 12
        if detMatrix(keyMatrix1) == 0 or detMatrix(keyMatrix2) == 0:
            print("Определитель матрицы равен 0")
            return 22

    if len(text) == 0:
        print("Текст не введён")
        return 3
    return 0


def hillCode(code, matrix):
    triplex = list()
    outCode = list()
    buf = 0
    while(len(code) >= 3):
        for q in range(3):
            triplex.append(code.pop(0))
        for i in range(3):
            for j in range(3):
                buf += matrix[i][j] * triplex[j]
            outCode.append(buf % 41)
            buf = 0
        triplex.clear()
        

    #print(outCode)#
    return outCode

def multipleMatrix(matrix1, matrix2):
    finalyMatrix = [[0] * 3 for i in range(3)]
    buf = 0
    for i in range(3):
        for j in range(3):
            for q in range(3):
                buf += matrix1[i][q] * matrix2[q][j]
            finalyMatrix[i][j] = buf
            buf = 0
            finalyMatrix[i][j] = finalyMatrix[i][j] % 41

    #print(finalyMatrix)
    return finalyMatrix


def hillCodeRec(code, matrix1, matrix2):
    
    mat1 = copy.deepcopy(matrix1)
    mat2 = copy.deepcopy(matrix2)
    triplex = list()
    outCode = list()
    buf = 0
    numOfTriplex = 0
    while(len(code) >= 3):
        for q in range(3):
            triplex.append(code.pop(0))
            ##
        numOfTriplex += 1
        if(numOfTriplex == 1):
            matrix = mat1
        elif(numOfTriplex == 2):
            matrix = mat2
        else:
            matrix = multipleMatrix(mat1, mat2)
            mat1 = mat2
            mat2 = matrix
            ##
        for i in range(3):
            for j in range(3):
                buf += matrix[i][j] * triplex[j]
            outCode.append(buf % 41)
            buf = 0
        triplex.clear()
        

    #print(outCode)#
    return outCode

def hillDecodeRec(code, matrix1, matrix2, mod = 0):
    
    mat1 = copy.deepcopy(matrix1)
    mat2 = copy.deepcopy(matrix2)
    triplex = list()
    outCode = list()
    buf = 0
    numOfTriplex = 0
    while(len(code) >= 3):
        for q in range(3):
            triplex.append(code.pop(0))
            ##
        numOfTriplex += 1
        if(numOfTriplex == 1):
            matrix = mat1
        elif(numOfTriplex == 2):
            matrix = mat2
        else:
            matrix = multipleMatrix(mat1, mat2)
            mat1 = copy.deepcopy(mat2) 
            mat2 = copy.deepcopy(matrix)
            ##
        if mod == 1:
            detf = detMatrix(matrix)
            
            matrix = matrixInversion(matrix, detf)
            
            ##
        for i in range(3):
            for j in range(3):
                buf += matrix[i][j] * triplex[j]
            outCode.append(buf % 41)
            buf = 0
        triplex.clear()
        

    #print(outCode)#
    return outCode


def matrixInversion(matrix, det):
    matrixZ = [[0] * 3 for i in range(3)]
    matrixZ[0][0] = matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]
    matrixZ[0][1] = -(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
    matrixZ[0][2] = matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]
    matrixZ[1][0] = -(matrix[0][1]*matrix[2][2]-matrix[0][2]*matrix[2][1])
    matrixZ[1][1] = matrix[0][0]*matrix[2][2]-matrix[0][2]*matrix[2][0]
    matrixZ[1][2] = -(matrix[0][0]*matrix[2][1]-matrix[0][1]*matrix[2][0])
    matrixZ[2][0] = matrix[0][1]*matrix[1][2]-matrix[0][2]*matrix[1][1]
    matrixZ[2][1] = -(matrix[0][0]*matrix[1][2]-matrix[0][2]*matrix[1][0])
    matrixZ[2][2] = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    matrixT = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            matrixT[j][i] = matrixZ[i][j]

    matrixMOne = [[0] * 3 for i in range(3)]
    na = createMOE(det, 41)
    for i in range(3):
        for j in range(3):
            matrixMOne[i][j] = na * matrixT[i][j]
            matrixMOne[i][j] = matrixMOne[i][j] % 41 
    
    #print (matrixMOne)#
    return matrixMOne


def test():
    code, keym = inputKeyText(0)
    det = detMatrix(keym)
    keyMaRev = matrixInversion(keym, det)
    cipher = hillCode(code, keym)
    print("Шивр:", end = " ")
    outputText(cipher)
    code = hillCode(cipher, keyMaRev)
    print("Расшифрованный открытый текст:", end = " ")
    outputText(code)

def codding():
    code, keyM = inputKeyText(0)
    cipher = hillCode(code, keyM)
    outputText(cipher)

def decodding():
    cipher, keyM = inputKeyText(1)
    det = detMatrix(keyM)
    keyMaRev = matrixInversion(keyM, det)
    code = hillCode(cipher, keyMaRev)
    outputText(code)

def test2():
    code, keyM1, keyM2 = inputKeyText(0, 1)

    
    det1 = detMatrix(keyM1)
    det2 = detMatrix(keyM2)
    keyMaRev1 = matrixInversion(keyM1, det1)
    keyMaRev2 = matrixInversion(keyM2, det2)
    cipher = hillCodeRec(code, keyM1, keyM2)
    
    print("Шивр:", end = " ")
    outputText(cipher)
    
    #code = hillDecodeRec(cipher, keyMaRev1, keyMaRev2)
    #print("Расшифрованный открытый текст:", end = " ")
    #outputText(code)

    code = hillDecodeRec(cipher, keyM1, keyM2, 1)
    print("Расшифрованный открытый текст:", end = " ")
    outputText(code)
    
def recCoding():
    code, keyM1, keyM2 = inputKeyText(0, 1)
    cipher = hillCodeRec(code, keyM1, keyM2)
    outputText(cipher)

def recDecoding():
    cipher, keyM1, keyM2 = inputKeyText(1, 1)
    code = hillDecodeRec(cipher, keyM1, keyM2, 1)
    outputText(code)

def job():
    #try:
    while True:
        comand = input("Что делать?  1 - Шифровать  2 - Расшифровывать  t - Тестировать  q - Выйти:")
        if(comand == '1'):
            command = input("Какой шифр использовать? 1 - Шифр Хилла  2 - Рекурентный шифр Хилла")
            if command == '1':
                codding()
            if command == '2':
                recCoding()
        elif(comand == '2'):
            command = input("Какой шифр использовать? 1 - Шифр Хилла  2 - Рекурентный шифр Хилла")
            if command == '1':
                decodding()
            if command == '2':
                recDecoding()
        elif(comand == 't'):
            test()
            test2()
        elif(comand == 'q'):
            print("Пока")
            return 0
        else:
            print("Неизвестная команда. Давай по новой")
    #except:
        #print("Упсссс....  Что-то пошло не так")

def main():
    job()
    #test2()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
