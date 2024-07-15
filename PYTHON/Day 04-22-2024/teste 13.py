#### Crie um programa que leia um número e, caso ele seja positivo, calcule e mostre:
### • O número digitado ao quadrado; ####
###v• A raiz quadrada do número digitado; ####

import math
num= float(input("Digite um número positivo ou negativo: "))

if (num>0):
    calculo1= num**2
    calculo2= (math.sqrt (num))
    print(f"O seu número({num}) ao quadrado é {calculo1} e a araiz dele é {calculo2}")