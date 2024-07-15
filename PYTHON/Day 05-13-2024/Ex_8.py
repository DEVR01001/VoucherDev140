# Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.


n =10
i =0
soma= 0

while i< n:
    soma+= int(input("Digite um número: "))
    i+= 1
media= soma/n
print(media)

