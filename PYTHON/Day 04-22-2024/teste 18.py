#### Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela ####
#### a média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, ####
#### onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o ####
#### programa termina. ####]


nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
media= (nota1+nota2)/2
if (nota1 >= 0.0 and nota1 <= 10.0 and nota2>= 0.0 and nota2<= 10.0):
    print(f"A nota 1 é de {nota1} e a segunda nota de {nota2} são válidas.")
    print(f"A média das notas são de {media} .")
else:
    print("As notas não são vállidas.")