# 2. Faça uma função que receba a data atual (dia, mês e ano) e exiba-a na tela no formato textual 
# por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000.





def Data_Extenso(dia,mes,ano):
    lista_data_extenso= {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}
    print(f"{dia} de {(lista_data_extenso[mes])} de {ano}")


Data_Extenso(1,3,2000)

