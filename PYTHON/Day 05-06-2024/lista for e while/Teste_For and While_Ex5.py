# Crie um progama que receba a palavra FELICIDADE e imprima a posição de cada letra da palvra e informe
# qual letra está sendo impressa na posição x. Após imprima a mensagem que o programa foi finalizado


lista= input("Digite uma palavra: ")

i= 0

while i < len(lista):
    print(f"posição {i} a letra  {lista[i]}")
    i= i + 1

print("Programa finazalizado")