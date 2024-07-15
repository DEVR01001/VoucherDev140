#### Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim ####
#### como a diferença existente entre ambos. ####

num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))
calculo1= num1 - num2
if (num1 > num2):
    print(num1)
    print(f"A diferença entre eles é de {calculo1}")
else:
    calculo2= num2 - num1
    print(num2)
    print(f"A diferença entre eles é de {calculo1}")

    