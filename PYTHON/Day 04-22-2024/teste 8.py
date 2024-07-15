#### Faça um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou ####
#### V- Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ###
#### ou "Valor Inválido!", conforme o caso.####

turno= input("Digite qual turno você estuda (M) para Matutino, (V) para Vespertino e (N) para noturno: ")
if (turno == "M"):
    print("Bom Dia!")
elif(turno== "V"):
    print("Boa tarde!")
else:
    print("Boa Noite!")

