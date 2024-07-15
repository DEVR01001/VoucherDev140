# Um pescador, comprou um PC para controlar o rendimento diário de seu trabalho. Toda vez ele traz um peso de peixes maior que o estebelecendo pelo regulamento de pesca
# do MS (50 kg) deve pagar uma multa de R$ 4, 00 por quilo excendete. O pescador precisa que você crie uma função para ler a quantidade de peixes e calcular o excesso. Grava 
# na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que o pescador deverá pagar. Imprima os dados do programa com as 
# mensagens adequadas.



def calcular_qunt_peixes(quantidade_pexixes):
    multa_excesso= 4.00
    peso_peixe= 1.5
    calculo= quantidade_pexixes*peso_peixe
    if calculo > 50:
        i= calculo
        valor_excesso= 0
        while i > 50:
            valor_excesso+=4
            i-= 1.5
        fim= print(f"O kilo total de peixes é {calculo}(kg), com cada peixe sendo 1.5(kg) e o excesso é {valor_excesso}R$")
        return fim
    else:
        fim= print(f"A quantidade total de peixes é {calculo}(kg), sendo cada peixe com 1.5(kg), sem excesso.")
        return fim
    

peixes= int(input("Digite a quantidade de peixes recolhidos: "))
total= calcular_qunt_peixes(peixes)






# def calcular_exesso_e_multa(peso_peixe):
#     limite_peso= 50
#     valor_multa_por_quilo= 4

#     excesso= max(0, peso_peixe -limite_peso)
#     multa= excesso *valor_multa_por_quilo
#     print(f"O Peso total de peixes: {peso_peixe}")
#     if excesso >0:
#         print(f"Peso total de peixes: {excesso}")
#         print(f"Valor da multa: {multa}")
#     else:
#         print(f"Não ha, excesso d epeixe")
#         print(f"Valor da Multa R% 0.00")

# peso_peixes = float(input("Digite o peso total de peixes em (kg): "))
# calcular_exesso_e_multa(peso_peixes)
