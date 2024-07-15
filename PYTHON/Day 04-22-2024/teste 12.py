#### Leia um número real. Se o número for positivo imprima a raiz quadrada. Caso contrário imprima ####
#### o número ao quadrado. ####


import math

num= float(input("Digite um número postivo ou negativo: "))

if (num >= 0):
    calculo1= (math.sqrt(num))
    print(f"A raiz desse número é: {calculo1}")
elif(num < 0):
    calculo2= num**2
    print(f"O número ao quadrado é {calculo2}")
    