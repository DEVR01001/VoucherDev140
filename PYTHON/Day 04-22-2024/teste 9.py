#### Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor ####
#### de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser ####
#### vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, faça um ####
#### algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda. ####

valorpeça= float(input("Digite o valor da peça:"))

if(valorpeça < 50.00):
    porcentagemdevenda45= valorpeça*(45/100)
    valortotal45= porcentagemdevenda45 + valorpeça
    print(f"O valor a ser vendido é de {valortotal45}R$")
else:
    porcentagemdevenda30= valorpeça*(30/100)
    valortotal30= porcentagemdevenda30 + valorpeça
    print(f"O valor a ser vendido é de {valortotal30}R$")
