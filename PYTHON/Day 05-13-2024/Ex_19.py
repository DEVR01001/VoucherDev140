# Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima dos algarismos que compôem o número.

num= int(input("Digite um número: "))

if num >100 or num <9999:
    print(f"Os algoritmo do número: {num}")
else:
    print("Número fora de intervalo espefcificado")
while num>0:
    algoritmo= num% 10
    print(algoritmo)
    num//=10
    

