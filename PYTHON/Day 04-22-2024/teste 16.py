#### Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números ####
#### forem iguais, imprima a mensagem: Números iguais ####



num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))
if (num1 > num2):
    print(num1)
else:
    print(num2)
if( num1 == num2):
    print("Números iguais")