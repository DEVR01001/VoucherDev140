# Crie um programa que leia um número inteiro N e depois imprimia os N primeiros números naturais ímpares.

num= (int(input("Digite um número: ")))

i = 1

while i < num:
    print(i)
    i += 2

print(100*"=")

num= int(input("Digite um número: "))
for i in range(1, num, 2):
    print(i)