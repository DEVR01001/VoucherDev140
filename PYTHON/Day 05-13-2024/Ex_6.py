# Escreva um programa que peça ao úsuario para digitar 10 valores e some-os.
 

n =10
i =0
soma= 0

while i< n:
    soma+= int(input("Digite um número: "))
    i+= 1
    
print(soma)