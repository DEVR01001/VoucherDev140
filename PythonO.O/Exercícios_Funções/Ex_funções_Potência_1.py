# 1- Crie uma função que receba dois números como parâmetros e mostre a potência do número 
# elevado a n vezes, exemplo: 
# pot(2,3)
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8


def Pot(num1,num2):
    for i in range(1,num2+1):
        print(f"{num1} ** {i} = {num1**i}")


Pot(2,3)



