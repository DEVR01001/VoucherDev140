#### Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se ####
#### forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos: ####
#### • O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados. ####
#### • Chama-se equilátero o triângulo que tem três lados iguais. ####
#### • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais. ####
#### • Recebe o nome de escaleno o triângulo que tem os três lados diferentes. ####



num1= float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
num3= float(input("Digite o terceiro número: "))

if( num1 == num2 == num3):
    print("É um triangulo equilátero")
elif (num1== num2 or num1== num3 or num2==num1 or num2==num3 or num3==num1 or num3== num2):
    print("É um triangulo isóceles")
elif (num1!=num2!=num3):
    print("É um triangulo escaleno")