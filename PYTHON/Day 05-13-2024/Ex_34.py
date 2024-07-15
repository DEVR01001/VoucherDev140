# Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os números 
# pares na lista PAR e os números IMPARES na lsita ímapr.Imprima os tres vetores.


lista =[]
impar = []
par = []

i = 0

while i < 20:
    num = int(input("Digite um número: "))
    # validar se é par ou impar
    if num % 2 ==0:
        par.append(num)
    else:
        impar.append(num)
    lista.append(num)
    i+=1

print(lista)
print(par)
print(impar)