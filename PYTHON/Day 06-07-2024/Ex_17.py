# Uma rede de churrascaria realiza promoções semanais e precisa automatizar os descontos de acordo com o dia da semana 
# (terça-feira 10%, quarta-feira 15%, quinta-feira 20%). Crie uma função que calcule o preço final do consumo por pessoa.
# Considere a taxa de atendimento e o couvert, caso o cliente concorde com o pagamento. Utilize argumentos nomeados **kwargs, 
# Exemplo de chamada da função:​

# desconto(‘quinta-feira’,valor=99.90,taxa=0.10,couvert=15)

# Conta S/Taxa: 79.92
# Conta C/ Taxas:
# Rodizio: 79.92
# Taxa Serviço: 7.99
# Couvert: 15
# Total R$: 102.91


def calculo_valor(**valor_sem_taxa):
    couvert= 15
    taxa_serviço= 0.10*valor_sem_taxa
    tarifa_dia_semana= {"terça": 0.10, "quarta": 0.15, 'quinta': 0.20}
    calculo_terça= valor_sem_taxa*tarifa_dia_semana["terça"]
    calculo_quarta= valor_sem_taxa*tarifa_dia_semana["quarta"]
    calculo_quinta= valor_sem_taxa*tarifa_dia_semana["quinta"]



dic= []
while dic < 1:
    valor_conta= float(input("Digite o valor da conta: "))
    dic.append(valor_conta)


    








