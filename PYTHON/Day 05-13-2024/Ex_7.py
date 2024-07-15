# Escreva um programa que lei 10 inteiros e imprima sua média

num_lista= []
while (len(num_lista)) < 10:
    num_lista.append(int(input("Digite um número: ")))

print(num_lista)
print(f"A média dess lista é: {sum(num_lista) / len(num_lista)}")

print(100* "=")

n =10
i =0
soma= 0

while i< n:
    soma+= int(input("Digite um número: "))
    i+= 1
media= soma/n
print(media)