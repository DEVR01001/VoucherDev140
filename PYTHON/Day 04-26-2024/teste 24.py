#### A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 ####
#### até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame ####
#### final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de ####
#### Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela ####
#### se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi ####
#### aprovado. Faça todas as verificações necessárias. ####



nota1= float(input("Digite a nota do trabalho de laboratório: "))
nota2= float(input("Digite a nota da avaliação semestral : "))
nota3= float(input("Digite a nota do exame: "))

peso1= 2
peso2= 3
peso3= 5

media= (nota1*peso1 + nota2*peso2 + nota3*peso3)/ (peso1+peso2+peso3)

if (media>= 0 and media<=2.9):
    print(f"Aluno reprovado, média {media}")
elif( media>= 3 and media<=5.9):
    print(f"Aluno de recuperção, média {media}")
elif( media>= 6):
    print(f"Aluno aprovado, média {media}")
