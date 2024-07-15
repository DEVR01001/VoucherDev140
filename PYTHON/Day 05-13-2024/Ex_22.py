# Escreva um programa que permita a qualquer aluno introduzir, pelo teclado,uma sequência de 
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente
# média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não fornecido
# ao programa, o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.



quantidades_notas= int(input("Digite quantas notas são: "))
soma= 0
i = 0
while i < quantidades_notas:
    notas= float(input("Digite sua nota: "))
    if notas < 0 and notas > 10:
        print("Valor digitado inválido")
        break
    else:
        print(notas)
        soma+=notas
        i+=1
        media= soma / quantidades_notas
print(f"A média de suas notas é : {media}")


 