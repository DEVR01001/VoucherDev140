###  lanchonete do Gauchão vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias ###
### de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ###
### ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo ###
### em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades ###
### (em quilos) de queijo, presunto e carne necessários para compra.###
quantidadesanduiche= int(input("Digite a quantidade de sanduiches: "))
hambuger = 100
conversaohambuger= hambuger/1000
queijo= 50
conversaoquijo= queijo/1000
presunto= 50
conversaopresunto= presunto/1000
sanduichequeijo= (2*conversaoquijo)*quantidadesanduiche
sanduichepresunto= (1*conversaopresunto)*quantidadesanduiche
sanduichehambuger= (1*conversaohambuger)*quantidadesanduiche
print(f"Você terá que comprar de {sanduichequeijo}kg de queijo, {sanduichepresunto}kg de presunto e {sanduichehambuger}kg de hambuger.")
