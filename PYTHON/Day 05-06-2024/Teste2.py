numeros= [ 23, 45, 87, 24, 11]
print(numeros)
print(100*"-")
print(f"O tamanho da lista é: {len(numeros)}")
print(100*"-")
numeros.append(3.45)
numeros.append(19.3)
numeros.append(123.34)
numeros.append(566.65)
numeros.append(10.10)
print(numeros)
print(100*"-")
numeros.pop()
numeros.pop()
print(numeros)
print(100*"-")
print(f"O tamanho d a lista é: {len(numeros)}")
print(100*"-")
lista_ordena= sorted(numeros)
print(f"A lista ordena fica: {lista_ordena}")
print(100*"-")
print(f"Maior número da lista é: {max(numeros)}")
print(min(numeros))
print(100*"-")
lista_invertida= (sorted(numeros, reverse=True))
print(f"A lista ivertida é: {lista_invertida}")
print(100*"-")
print(f"A soma da lista é: {sum(numeros)}")
print(f"A média da lista é: {sum(numeros)/(len(numeros))}")
print(100*"-")
numeros.insert(0,657)
numeros.insert(1,34)
print(numeros)
      
      