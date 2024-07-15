# Crie um programa que receba dois números. Calcule e mostre:

# * a soma dos números pares desse intervalo de números, incluindo os números digitados;
# * a multiplicação dos números ímapres desse intervalo, incluindo os digitados;



numero_1= int(input("Digite um número: "))
numero_2= int(input("Digite outro número: "))

soma= 0
i =0 
pares= 0
impares= 1
for i in range(numero_1, numero_2 +1):
    if i % 2 ==0:
        print(i)
        pares+= i
    
    else:
        impares*= i


print(pares)
print(impares)

