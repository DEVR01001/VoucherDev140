# Faça um Programa que leia um vetor de 10 carteres, e diga quabtas consoates foram lidas. Imprima as consoantes.




palavra = input("DIGITE UMA PALAVRA QUALQUER: ").upper()

vogais = ['A','E','I','O','U']
consoantes = []
i = 0

while i < len(palavra):
    if palavra[i] not in vogais:
        consoantes.append(palavra[i])
        i = i + 1
    else:
        i = i + 1

print("LISTA DE CONSOANTES: ",consoantes)
print("QUANTIDADE DE CONSOANTES: ",len(consoantes))

