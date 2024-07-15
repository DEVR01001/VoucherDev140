# Elabore um algoritmo para fazer cálculos de potenciação. Ou seja, x^y,(Exemplo: 3^4= 3x3x3x3).Seu algoritmo
# deverá solicitar que o usuário entre com o valor da base(x) e do expoente(y) e apresentar o resultado do cálculo 
# sem ultilizar os operadores(por exemplo **). Para resolver o problema ultilize estrutura de repetição.

num1= int(input("Digite um número: "))
num2= int(input("Digite um expoente: "))

result=1
cont=0
while num2> cont:
    result*=num1
    cont+=1
print(f"A base do {num1}**{num2}, o resulatado é: {result}")
    
