#### . Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas ####
#### no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados ####
#### 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: ####
#### - salário bruto. ####
#### - quanto pagou ao INSS. ####
#### - quanto pagou ao sindicato. ####
#### - o salário líquido. ####
#### calcule os descontos e o salário líquido, conforme a tabela abaixo ####

#### IR (11%)             INSS (8%)           Sindicato (5 %) ####
#### - Salário Bruto : R$ ####
#### - Salário Líquido: R$ ####
#### Obs.: Salário Bruto - Descontos = Salário Líquido ####




ganhosporhora= float(input("Digite quanto você ganha por hora no mês: "))
horastrabalhadas= int(input("Digite quantas horas você trabalha por hora: "))

salariobruto= ganhosporhora*horastrabalhadas
inss= salariobruto* (8/100)
sindicato= salariobruto* (5/100)
impostoderenda= salariobruto* (11/100) 

salarioliquido= (((salariobruto - inss) - sindicato)- impostoderenda)

print(f"O sálario bruto é de {salariobruto}R$ \n Foi descontado {inss}R$ para o INSS \n Foi descontado {sindicato}R$ para o sindicato \n Sálario liquido de {salarioliquido}R$")