# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. 
# O programa tem que retornar o maior e o menor número lido. 




n= 0

cont= True
num_lista= []
while cont:
    if n >= 0:
        n = (int(input("Digite um número positivo (Ou negativo para sair): ")))
        num_lista.append(n)
    else: 
        break
num_lista.pop() 

print(f"O maior número é {max(num_lista)} e o menor é {min(num_lista)}.")

