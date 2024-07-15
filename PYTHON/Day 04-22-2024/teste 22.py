#### Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma ####
#### de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se ####
#### o número lido não for maior do que zero, o programa termina com a mensagem “Número ####
#### inválido" ####


n = input("Digite um número inteiro: ") 

print(len(n))
algorismo1= int(n[0])
algorismo2= int(n[1])
algorismo3= int(n[2])
soma= algorismo1+algorismo2+algorismo3
print(f"A soma dos números é de {soma}")