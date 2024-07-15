# Escreva um algoritmo que leia um vetor com 10 posições de números inteiros.
# Em seguida receba um novo valor do usuário e verifique se este valor se encontra no vetor.


lista = []

while len(lista) < 10:
    n= int(input("Digite um número inteiro: "))
    lista.append(n)
n_lista= int(input("Digite um número inteiro para verificar se ele esta na lista: "))

i=0
while i < len(lista):
    if lista[i] == n_lista:
        print(f"Está na lista {n_lista}")
        break
    else:
        i+=1
print("Não encontramos o número")
