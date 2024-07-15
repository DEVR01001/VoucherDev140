#### Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a ####
#### tabela abaixo: ####

#### IMC         | Classificação ####
#### < 18,5      | Abaixo do Peso ####
#### 18,6 - 24,9 | Saudável ####
#### 25,0 - 29,9 | Peso em excesso ####
#### 30,0 - 34,9 | Obesidade Grau I ####
#### 35,0 - 39,9 | Obesidade Grau II (severa) ####
#### ≥ 40,0      |Obesidade Grau III (mórbida) ####


altura= float(input("Digite sua altura em metros: "))
peso= float(input("Digite seu peso em kg: "))
imc= peso/(altura*altura)

if(imc <= 18.5):
    print(f"Seu imc é {imc}, e você está abaixo do peso")
elif(imc >= 18.6 and imc <=24.9):
    print(f"Seu imc é {imc}, e você está saudável")
elif(imc >= 25.0 and imc <=29.9):
    print(f"Seu imc é {imc}, e você está em peso em excesso")
elif(imc >=30 and {imc} <=34.9):
    print(f"Seu imc é {imc}, e você está obesidade Grau I")
elif(imc >= 35.0 and imc <= 39.9):
    print(f"Seu imc é {imc}, e você está obesidade Grau II (severa)")
elif(imc >= 40.0):
    print(f"Seu imc é {imc}, e você está obesidade Grau III (mórbida)")
