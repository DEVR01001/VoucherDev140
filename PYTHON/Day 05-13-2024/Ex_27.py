# Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do Fatorial:
# A! e seu resultado. Ex: 5!=5x4x3x2x1=120

num=int(input("Digite um núemro: "))
resultado=1

for i in range(1, num+1):
    resultado*=i

print(F"O resultado da fatoração de {i} é {resultado}")

