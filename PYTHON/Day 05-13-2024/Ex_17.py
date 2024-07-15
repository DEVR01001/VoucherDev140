# Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.


num = int(input("Digite um núemro: "))

i = 0
soma= 0
while i <= num:
    print(i)
    soma+=i
    i += 1
print(soma)




