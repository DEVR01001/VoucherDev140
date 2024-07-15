

a= int(input("Digite o coeficiente a: "))
b= int(input("Digite o coeficiente b: "))
c= int(input("Digite o coeficiente c: "))

import math
formula= (a**2)+b+c
delta= (b**2) - (4*a*c)


if( delta<0): 
    print("Não existe raiz")
elif( delta == 0):
    x1= math.sqrt(delta)
    x1_2= (-b + x1)/ 2*a
    x2= math.sqrt(delta)
    x2_2= (-b - x2)/ 2*a
    print(f"{x1_2 or x2_2}, raiz única")
elif( delta>- 0 ):
    x1= math.sqrt(delta)
    x1_2= (-b + x1)/ 2*a
    x2= math.sqrt(delta)
    x2_2= (-b - x2)/ 2*a
    print(f" {x1_2} e {x2_2}, raizes reais")