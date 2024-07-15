#### Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que considera o salário atual e o tempo  ####
#### de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os  ####
#### funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus ####
#### adicional de salário. Crie um programa que leia: ####
#### • o valor do salário atual do funcionário; ####
#### • o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa). ####

#### Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do ####  
#### salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento. #### 
#### Salário Atual    |Reajuste (%)| Tempo de Serviço | Bônus #### 
#### Até 500,00       |25%         | Abaixo de 1 ano  |Sem bônus #### 
#### Até 1000,00      |20%         | De 1 a 3 anos    |100,00 #### 
#### Até 1500,00      |15%         | De 4 a 6 anos    |200,00 #### 
#### Até 2000,00      |10%         | De 7 a 10 anos   |300,00 #### 
#### Acima de 2000,00 |Sem reajuste| Mais de 10 anos  |500,00 #### 


salario= float(input("Digite o sálario atual: "))
tempodeserviço= int(input("Digite o tempo de serviço em anos na empresa: "))

if( salario > 0 and salario <= 500 and tempodeserviço < 1):
    reajuste= salario* (25/100)
    salariofinal= salario+reajuste
    print(f"Seu sálario final é de {salariofinal} R$")
elif( salario > 500 and salario <= 1000 and tempodeserviço >= 1 and tempodeserviço <= 3):
    reajuste= salario* (20/100)
    bonus= 100
    salariofinal= salario+reajuste+bonus
    print(f"Seu sálario final é de {salariofinal} R$")
elif( salario > 1000 and salario <= 1500 and tempodeserviço >=4 and tempodeserviço <= 6):
    reajuste= salario* (15/100)
    bonus= 200
    salariofinal= salario+reajuste+bonus
    print(f"Seu sálario final é de {salariofinal} R$")
elif( salario > 1500 and salario <= 2000 and tempodeserviço >=7 and tempodeserviço <= 10):
    reajuste= salario* (10/100)
    bonus= 300
    salariofinal= salario+reajuste+bonus
    print(f"Seu sálario final é de {salariofinal} R$")
elif( salario > 2000 and tempodeserviço > 10):
    bonus= 500
    salariofinal= salario+bonus
    print(f"Seu sálario final é de {salariofinal} R$")

