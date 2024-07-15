# Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos 
# e segundos, e os converta em segundos.


def Convert_segund(horas,min,seg):
    calculo= (horas*360)+(min*60)+seg
    return calculo

print(f"{Convert_segund(5,30,50)} segundos.")


