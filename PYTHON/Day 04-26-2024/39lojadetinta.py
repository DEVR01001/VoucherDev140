#### Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros #### 
#### quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros #### 
#### quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 #### 
#### litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os #### 
#### respectivos preços em 3 situações: 

#### #### - comprar apenas latas de 18 litros; #### 
#### - comprar apenas galões de 3,6 litros; #### 
#### - misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre #### 
#### arredonde os valores para cima, isto é, considere latas cheias #### 

import math

# Função para calcular a quantidade de tinta necessária em litros
def calcular_tinta(area):
    return area / 6 * 1.1  # 10% de folga

# Função para calcular o preço das latas de 18 litros
def preco_latas(area):
    tinta_necessaria = calcular_tinta(area)
    latas = math.ceil(tinta_necessaria / 18)
    preco_total = latas * 80
    return latas, preco_total

# Função para calcular o preço dos galões de 3,6 litros
def preco_galoes(area):
    tinta_necessaria = calcular_tinta(area)
    galoes = math.ceil(tinta_necessaria / 3.6)
    preco_total = galoes * 25
    return galoes, preco_total

# Função para calcular o preço misturando latas e galões
def preco_misturado(area):
    tinta_necessaria = calcular_tinta(area)
    latas = math.floor(tinta_necessaria / 18)
    tinta_restante = tinta_necessaria - latas * 18
    galoes = math.ceil(tinta_restante / 3.6)
    preco_total = latas * 80 + galoes * 25
    return latas, galoes, preco_total

# Função principal
def main():
    area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

    latas, preco_latas_total = preco_latas(area)
    galoes, preco_galoes_total = preco_galoes(area)
    latas_misturadas, galoes_misturados, preco_misturado_total = preco_misturado(area)

    print(f"\nQuantidade de tinta necessária:")
    print(f"Comprar apenas latas de 18 litros: {latas} latas")
    print(f"Comprar apenas galões de 3,6 litros: {galoes} galões")
    print(f"Misturar latas e galões:")
    print(f"  Latas: {latas_misturadas}, Galões: {galoes_misturados}")

    print("\nPreços:")
    print(f"Comprar apenas latas de 18 litros: R$ {preco_latas_total:.2f}")
    print(f"Comprar apenas galões de 3,6 litros: R$ {preco_galoes_total:.2f}")
    print(f"Misturar latas e galões: R$ {preco_misturado_total:.2f}")

if __name__ == "__main__":
    main()