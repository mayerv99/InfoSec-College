from random import random

def deslocamento(registrador, shiftar, tipo):
    retorno = registrador[0]

    if (shiftar == 1):
        if (tipo == 0):
            xor = registrador[31] ^ registrador[6] ^ registrador[4] ^ registrador[2] ^ registrador[1] ^ registrador[0]
        else:
            xor = registrador[31] ^ registrador[6] ^ registrador[5] ^ registrador[1]

        for i in range(0, 31):
            registrador[i] = registrador[i + 1]

        registrador[31] = xor

    return retorno

cabeca = []
gerador1 = []
gerador2 = []
caractere = ""
arquivo = open("lfsr.txt", "w", encoding="utf-8")

senha = input("Digite 4 letras: ")
for i in range (0, len(senha)):
    alimentaVetor = str(bin(ord(senha[i])))
    if (len(alimentaVetor) == 9):
        alimentaVetor = alimentaVetor[2:]
    print(senha[i])
    print(ord(senha[i]))
    print(bin(ord(senha[i])))
    for j in range (0, len(alimentaVetor)):
        cabeca.append(alimentaVetor[j])

print(cabeca)

#for i in range(0, 32):
#    cabeca[i] = int(2 * random())
#    gerador1[i] = int(2 * random())
#    gerador2[i] = int(2 * random())

for i in range(-1000, 1000):
    if deslocamento(cabeca, 1, 0) == 0:
        operando1 = deslocamento(gerador1, 1, 0)
        operando2 = deslocamento(gerador2, 0, 1)
    else:
        operando1 = deslocamento(gerador1, 0, 0)
        operando2 = deslocamento(gerador2, 1, 1)
    
    caractere += str(operando1 ^ operando2)

    if (i % 8) == 7:
        print(caractere + " " + str(int(caractere, 2)) + " " + chr(int(caractere, 2)))
        arquivo.write(str(chr(int(caractere, 2))))
        caractere = ""