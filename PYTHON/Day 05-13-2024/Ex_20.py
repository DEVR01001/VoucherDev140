# Ler uma sequêcia de números inteiros e determinar se eles são pares ou informando o número de dados lidos e 
# números de valores pares. O processo termina quando for digitado o número 0.






dados=0
pares=0

while True:
    numero= int(input("Digite um número: "))
    if numero ==0:
        break
    dados+=1
    if numero % 2 == 0:
        pares+=1

print("O Valor de numeros pares é:", pares)
print("O Valor de números lidos é: ", dados)
