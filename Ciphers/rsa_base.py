import rsa


def createKey():
    pubkey, privkey = rsa.newkeys(1024)
    return pubkey, privkey

def encrypt(string :str, pubkey):
    while len(string) > 53:
        message = string[:53]
        string = string[53:]
        message = message.encode('utf8')
        crypto = rsa.encrypt(message, pubkey)

def decrypt(string :str, privkey):
    while len(string) > 53:
        message = string[:53]
        string = string[53:]
        message = message.encode('utf8')
        crypto = rsa.encrypt(message, pubkey)

pubkey, privkey = rsa.newkeys(1024)
a = 'qwertyuioasdfghjvwn0uйуцkzx cvbn'
message = a.encode('utf8')
crypto = rsa.encrypt(message, pubkey)


#print('crypto  ',crypto)
#print(len(crypto))

messageOut = rsa.decrypt(crypto, privkey)

#print(pubkey)
#print(privkey)
print(pubkey['e'], pubkey['n'])
print(privkey['d'], privkey['n'])
z = input('')
#print(messageOut.decode('utf8'))
