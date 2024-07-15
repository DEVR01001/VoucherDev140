# Crie uma função que receba uma lista como argumento, os valores da lista devem ser numéricos, por fim retorne a média desses valores


def lista (media_lista):
    calculo = sum(media_lista)/ len(media_lista)
    return calculo


lista_media= []
while len(lista_media) < 10:
    lista_media.append(int(input("Digite um número: "))) 


print(f"A média da lista é {lista(lista_media)}")



print("="*100)

#Exercicio Professor
def media(lista):
    soma= 0
    for num in lista:
        soma+=num
    media= soma /len(lista)
    return media

lista_de_numeros= [8,4,3,5,1,7,6,3,9,6]
x= media(lista_de_numeros)
print(x)