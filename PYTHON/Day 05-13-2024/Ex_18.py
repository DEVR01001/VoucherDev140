# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. 
# A quantidade de números a serem lidos deve ser fornecido pelo usuario.


quantidade_num= int(input("Digite a quantidades de núemros que você deseja: "))
lista_num= []

while quantidade_num > len(lista_num):
    lista_num.append(int(input("Digite um número: ")))
    
print(lista_num)
print(f"O maior núemro da lista é : {max(lista_num)}")