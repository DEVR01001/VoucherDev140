# Escreva um programa que calcule e escreva o valor de S: S=(1/1)+(3/2)+(5/3)+(7/4)...(99/50)
soma= 0
numerador = 1
denominador = 0
for n in range(1, 99+1,2):
    numerador = 2 * n - 1
    denominador +=1
    resultado = numerador / denominador
    soma+=resultado
    result = round(soma,2)

    print(f"Para n = {n}/{denominador}, o valor de S é {result}")

    