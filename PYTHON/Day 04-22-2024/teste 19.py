#### Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários ####
#### acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor ####
#### do seu salário líquido ####


hora= int(input("Digite a quantidades de horas trabalhas no mês: "))
salarioporhoras= 40.50*hora
if (salarioporhoras > 2500.00):
    impostoporcetagem= salarioporhoras*(11/100)
    imposto= salarioporhoras-impostoporcetagem
    print(f"O sálario líquido é de {imposto} R$ .")
else:
    print(f"O sálario dele líquido é de {salarioporhoras} R$ .")


    



