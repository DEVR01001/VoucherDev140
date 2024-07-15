# Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório 
# desses números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuáio digitou, um por linha. 




cont= 0

n= 0
soma= 0
lista=[]
for i in range(1,5):
    n=int(input("Digite um número: "))
    lista.append(n)
soma= sum(lista)

print(f"A soma dos número é {soma}")

for i in lista:
    print(i)
