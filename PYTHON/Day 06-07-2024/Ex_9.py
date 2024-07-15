# Crie uma função que receba como argumento uma lista, com vaalores de qualquer tipo. A função deve imprimir todos os elmentos da listas mnumeranndo-os. Exemplo:
# 1, pera 
# 2, Uva
# 3, Maça


def lista_palavras_organizadas ():
    lista_palvras= ['maça', 1, 'manteiga', 'casa', 76, 'ouvido', 'chave',  43, 12, 'cabeça', 9]
    for indice, i in enumerate(lista_palvras, start= 1):
        print(f" {indice}.{i}")


lista_palavras_organizadas()


print("="*100)
#Exercícios professor 

def imprime(lista):
    cont= 0
    while cont < len(lista):
        print(f"{cont+1}. {lista[cont]}")
        cont+=1



listadecompra= ['Mamao', 'Castanhas', 'Mel', 'Uva', 'Banana', 'Laranja']

imprime(listadecompra)