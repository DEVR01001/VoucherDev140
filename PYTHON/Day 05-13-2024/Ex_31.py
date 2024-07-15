# Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020
# recebeu aumento de 1.5%. A partir de 2021, os aumentos sempre correspodem ao dobro do 
# ano anterior. Faça um programa que determine o sálario atual do funcionário.


salario= 4000
aumeto_salario= (4000*1.5)/100
soma= salario + aumeto_salario
salario= soma


print(f"O sálario no ano de 2020 é {salario} R$")

aumentoporcentagem=1.5
cont = 2020
while cont < 2024:
    aumeto_salario=aumentoporcentagem*2
    divisao_salario= (salario*aumeto_salario)/100
    soma_aumento= salario+divisao_salario
    cont+=1
    aumentoporcentagem*=2
   
    print(f"O salário de {cont} é {soma_aumento}")
    


