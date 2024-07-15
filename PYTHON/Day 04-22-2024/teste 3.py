#### Faça um programa que leia 2 números inteiros e ####
#### 1 real. Calcule e mostre: o produto do primeiro ####
#### com a metade do segundo, a soma do triplo do ####
#### primeiro com o terceiro O terceiro número digitado ao cubo ####

num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))
num3= float(input("Digite um número deciamal: "))
num1multiplicaçaonum2= num1*(num2/2)
somatriplonum1 = (num1*3)+ num3
num3cubo= num3**3
print(f"O Resultado do primeiro calculo é ({num1multiplicaçaonum2}), o segundo é ({somatriplonum1}), e o terceiro é ({num3cubo})")


