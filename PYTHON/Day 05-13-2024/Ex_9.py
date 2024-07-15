# Escreva um progrsma que leia 10 números escreva o menor valor lido e o maior valor lido.



num_lista= []
while (len(num_lista)) < 10:
    num_lista.append(int(input("Digite um número: ")))
print(max(num_lista))
print(min(num_lista))
