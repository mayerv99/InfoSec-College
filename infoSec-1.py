# Symetric cipher, encrypt and decrypt with custom key

def runApp():
    entryText = input("Insira o texto: ")
    key = input("Insira a chave: ")
    option = input("Encrypt [E] or decrypt [D]? ")

    if option == "e":
        print(encrypt(entryText, key))
    elif option == "d":
        print(decrypt(entryText, key))
    else: 
        print('Insert a valid option')
        runApp()


def encrypt(text, key):
    i = 0
    encryptedData = ""
    while(i < len(text)): 
        textLetter = text[i]
        keyLetter = key[i % len(key)]
        
        letterXOR = ord(textLetter) ^ ord(keyLetter)

        if len(str(letterXOR)) == 2:
            character = str(letterXOR)
        else:
            character = "0" + str(letterXOR)
        
        encryptedData += character
        i += 1
        
    return encryptedData


def decrypt(encryptedData, key):
    i = 0
    text = ''

    while(i < len(encryptedData) -1):

        textLetter = encryptedData[i: i + 2]

        keyLetter = key[int(i/2 % len(key))]
        letterXOR = chr(int(textLetter) ^ ord(keyLetter))
        
        
        text += letterXOR

        i += 2

    return text

runApp()
