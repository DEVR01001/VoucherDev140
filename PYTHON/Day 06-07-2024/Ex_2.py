def somaImposto (taxaImposto,custo):
    Taxa_decimal = taxaImposto/100
    novo_custo= custo + (custo*Taxa_decimal)
    return novo_custo


taxa= 10
custo_inicial= 345
custo_final = somaImposto(taxa,custo_inicial)

print(f"O custo inicial era: {custo_inicial}$ ")
print(f"Com a taxa de imposto de {taxa}% , e o custo finla é: {custo_final}$")