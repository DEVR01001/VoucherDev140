########COmando entrada e saída de dados########
print("\nBem vindo ao cadastramento de vencimento do cartão digital!!!")
name= input("\nDigite seu nome: ")
dayvencimento= int(input("\nDigite o dia do vencimento do cartão: "))
monthvencimento= int(input("\nDigite o mês de vencimento do seu cartão: "))
valuefatura= float(input("\nDigite  valor da fatura do seu cartão: "))
print(f"\nO cliente {name} possuem uma fatura no cartão no valor de R$({valuefatura}) com dia de vencimento {dayvencimento} do mês {monthvencimento}")