#### Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem ####
#### crescente. Caso contrário, imprima não está em ordem crescente. ####



num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))
num3= int(input("Digite um terceiro número inteiro: "))


if (num1 < num2 and num1<num3):
    print(num1)
    print(num2)
    print(num3)
    print("Estão em ordem crescente.")
else:
    print("Não estão em ordem crescente.")
