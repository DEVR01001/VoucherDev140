# Lista

numeros= [23, 45, 70, 64, 65, 24]
frutas= ["banana", "maça", "pera", "uva", "goiaba"]

print(len(numeros))
print(numeros[0])
print(numeros[3])

print(100*"=")
print(len(frutas))
print(frutas[0])
print(frutas[3])

print(100*"=")
print(numeros[2] + numeros[3]) # Operações de listas
print(numeros[2] * numeros[3]) 
print(numeros[2] - numeros[3]) 
print(numeros[2] / numeros[3]) 

print(100*"=")
print(f"Soma dos Números: {sum(numeros)}")
print(f"Maior dos Números: {max(numeros)}")
print(f"Menor dos Números: {min(numeros)}")

print(100*"=")
listas_ordenada= sorted(numeros) # Função para deixar ordenada da lista
print(listas_ordenada)

print(100*"=")
print(reversed(numeros))

print(100*"=")
print(sum(numeros) / len(numeros)) #Média dos números da lista

print(100*"=")
indice= numeros.index(24) #Função para achar a posição de um número numa lista
print(indice)

print(100*"=")
numeros.pop() #Função para remover o último elemento da lista
print(numeros)
print(len(numeros))

print(100*"=")
numeros.insert(1,45) # Função para inserir um número em uma determida posição de uma lista (1 = posição, 45= número inserido)
print(numeros)

numeros.append(234)
print(numeros)  ## Função para inserir um número no final de uma lista (234 = número inserido)

print(100*"=")
for item in frutas: #Função para modificar ou imprimir os itens de uma determinada lista
    print(item)