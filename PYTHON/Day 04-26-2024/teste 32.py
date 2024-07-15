#### Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias: ####
#### Categoria Idade ####
#### Infantil A |5 a 7 ####
#### Infantil B |8 a 10 ####
#### Juvenil A  |11 a 13 ####
#### Juvenil B  |14 a 17 ####
#### Sênior     |maiores de 18 anos ####



idade= int(input("Digite sua idade: "))

if (idade>= 5 and idade<= 7):
    print(f" Sua categoria é a infantil A")
if (idade>= 8 and idade<= 10):
    print(f" Sua categoria é a infantil B")
if (idade>= 11 and idade<= 13):
    print(f" Sua categoria é a juvenil A")
if (idade>= 14 and idade<= 17):
    print(f" Sua categoria é a juvenil B")
if (idade> 18):
    print(f" Sua categoria é a sênior")

