#### Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do ####
### número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido. ####

import math

num= float(input("Digite um número postivo ou negativo: "))

if (num >= 0):
    calculo1= (math.sqrt(num))
    print(f"A raiz desse número é: {calculo1}")
elif(num < 0):
    print("O número é inválido")
    