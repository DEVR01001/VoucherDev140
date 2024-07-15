# Crie uma função que efetue o cálculo do sálario e como retorno teremos o valor  a ser pago conforme o numero de horas trabalhadas. Considere a carga horária de 40H por 
# semana como base, caso ultrapasse o limite de 40 h, o funcionário deve receber 50% a mais por hora excedente.


def salario(carga_horas, valor_horas):
    carga_horaria_base= 40
    if carga_horas <= 40:
        salario_total= carga_horas*valor_horas
        return salario_total
    else:
        horas_extras= carga_horas - carga_horaria_base
        pagamento_extra= horas_extras*(valor_horas*1.5)
        salario_base= carga_horaria_base*valor_horas
        total= salario_base+pagamento_extra
        return total

quant_de_horas_trabalhadas= float(input("Digite a quantidades de horas trabalhadas: "))
valor_pago_por_hora= float(input("Digite o valor a ser pago por horas trabalhadas: "))
print(f"O valor a ser pago pela quantidade {quant_de_horas_trabalhadas} horas é {salario(quant_de_horas_trabalhadas,valor_pago_por_hora)}")