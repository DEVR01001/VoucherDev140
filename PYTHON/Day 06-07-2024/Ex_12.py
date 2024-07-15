# Crie uma função que receba comoa argumento a potencia elétrica de determinado aparelho e o tempo ligado e retorne o consumo em KMh em seguida chame outra função
# para calcular a conta de energia, levando em consideração o consumo e o valor do KWh como argumentos.


def potencia_eletrica(potencia_aparelho,tempo_ligado):
    watss_energia= potencia_aparelho
    tempo_de_funcionamento_aparelho= tempo_ligado
    calculo_KMh= (watss_energia*tempo_ligado)/1000
    return calculo_KMh


def consumo_mensal_energia(consumo_aparelho_KMh):
    consumo_aparelho_KMh= consumo_aparelho_KMh*30
    calculo_valor_KMh_aparelho= consumo_aparelho_KMh*0.50
    print_valor_kMh= print(f"O valor que esse aparelho gasta por mês é {calculo_valor_KMh_aparelho} R$")



print("Vamos calcular o consumo de ernegia!!!")
kmw= int(input("Digite a quantidade de waats do aparelho:"))
tempo_ligado=  float(input("Digite o tempo que o aparelho fica ligado por dia: "))

result_final= potencia_eletrica(kmw,tempo_ligado)
print(f"O consumo de Kmh desse aparelho por dia é {result_final}")
consumo_mensal_energia(result_final)



# Exercício Professor
def calcular_valor(consumo,preço):
    valor= consumo*preço
    return valor

def calcula_consumo(potencia,horas,preço):
    consumo= potencia*horas/1000
    conta = calcular_valor(consumo,preço)
    return conta # return -> devolve o vqlor calculado para a 


potencia= int(input("Digite a potência do aparelho: "))
tempo= int(input("Quanto foi ultilizado no Mês: "))
preco= float(input("Valor do Kmh: "))


banho= calcula_consumo(potencia,tempo,preco) # A funão retorna o valor do consumo 
print(f"R$: {banho}")
