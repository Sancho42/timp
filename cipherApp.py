import Ciphers.VigenereCipher as ViCi
import Ciphers.affinityEncryption as affine
import  Ciphers.HillEncryption as hill
import  Ciphers.RSA as myRSA


def VigenereCipher(INText, INKeys, EncryptionMode = True):
    try:
        code, key = ViCi.inputTextKey(0, INText, INKeys)
        if EncryptionMode is True or EncryptionMode == 'encryption':
            cipher = ViCi.VigenereCipher(code, key, True) # если ввести ключ из неподходящих символов
                                                          # вылетит ошибка, так как key станет равен 'a'
        else:
            cipher = ViCi.VigenereCipher(code, key, False)
        return ViCi.outputText(cipher, consoleOutput=False)
    except:
        return 'я делаль делаль, но не получилось ('

def affinityEncryption(INText, INKeys, EncryptionMode = True):
    try:
        INKeys = INKeys.split(' ')
        sec = 0
        for i in INKeys:
            if i != '' and sec == 0:
                INKeys_a = int(i)
                sec = 1
            elif i != '' and sec == 1:
                INKeys_b = int(i)
                break

        INKeys_m = 41  # иначе никак
        INKeys_a = INKeys_a % INKeys_m
        INKeys_b = INKeys_b % INKeys_m
        if EncryptionMode is True or EncryptionMode == 'encryption':
            return affine.coding(INKeys_a, INKeys_b, INKeys_m, INText)
        else:
            return affine.decoding(INKeys_a, INKeys_b, INKeys_m, INText)
    except:
        return 'я делаль делаль, но не получилось ('

def HillEncryption(INText, INKeys, EncryptionMode=True):
    if INText != '' and INKeys != '':
        try:
            code, keyM = hill.inputKeyText(0, inputText=INText, inputKeys=INKeys)
            if EncryptionMode is True or EncryptionMode == 'encryption':
                cipher = hill.hillCode(code, keyM)

            else:
                det = hill.detMatrix(keyM)
                keyMaRev = hill.matrixInversion(keyM, det)
                cipher = hill.hillCode(code, keyMaRev)

            return hill.outputText(cipher, consoleOutput=False)
        except:
            return 'я делаль делаль, но не получилось ('
    return 'без входного текста и ключа ничего не получится'

def RSA(INText, INKeys, EncryptionMode=True):
    try:
        if EncryptionMode is True or EncryptionMode == 'encryption':
            code, key1, key2 = myRSA.inputTextKey(0, INText, INKeys)
            cipher = myRSA.RSA(code, key1, key2)
            return myRSA.outputCode(cipher, consoleOutput=False)
        else:
            code, key1, key2 = myRSA.inputTextKey(1, INText, INKeys)
            cipher = myRSA.RSA(code, key1, key2)
            return myRSA.outputText(cipher, consoleOutput=False)

    except:
        return 'я делаль делаль, но не получилось ('
