#### Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas ####
#### (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois ####
#### valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa. ####


num1= float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))

operação= input("Digite uma dessas 4 operações (+), (-), (*) ou (/): ")

if( operação == "+"):
    soma= num1+num2
    print(f"O resultado da soma foi de {soma}")
elif( operação == "-"):
    menos= num1-num2
    print(f"O resultado da subtração foi de {menos}")
elif( operação == "*"):
    vezes= num1*num2
    print(f"O resultado da multiplicação foi de {vezes}")

elif( operação == "/"):
    divisao= num1/num2
    print(f"O resultado da divisão foi de {divisao}")