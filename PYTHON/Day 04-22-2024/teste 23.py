#### Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda ####
#### prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi ####
#### aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos. ####



nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
nota3= float(input("Digite a terceira nota: "))

media= (nota1*10 + nota2*10 +nota3*20)/ 4

if (media >= 60):
    print(f"Sua média foi de `{media} pontos, você foi aprovado.")
else:
    print(f"Sua média foi de {media} pontos, você está reprovado.")