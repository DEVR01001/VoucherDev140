# Escreva um programa que leia um numero inteiro e calcule a soma de todos os divisores desse número, com execeção dele póprio.
# Ex: a soma dos divisores do número é 66 é:

# 1+2+3+6+11+22+33= 78

numero= int(input("Digite um número:"))
i= 1
soma= 0

while numero > 0:
    numero-=2
    if numero % i == 0:
        print(i)
        soma+= i
    i+=1
print(f"A soma dos divisores é:{soma}")