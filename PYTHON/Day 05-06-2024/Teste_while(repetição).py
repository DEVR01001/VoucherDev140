#ESTRUTUTAS DE REPETIÇÃO
#while= enquanto

contador= 0

while( contador <= 100):
    print(contador)
    contador= contador+1

print( 100*"=")

numero= 0
soma= 0

while( numero <=20):
    soma= soma + numero
    numero= numero + 1
    print(numero)

print(soma)

print( 100*"=")

lista= [24, 98, 33, 12, 85]
i = 0

while i < len(lista):
    print(f"Valor do contador {i} numeros na posição {lista[i]}")
    if lista[i] == 33:
        print("Achei o 33")
        break
    else:
        i = i + 1