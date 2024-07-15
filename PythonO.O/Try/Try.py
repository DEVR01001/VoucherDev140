# x =500
# y= 0

# try:
#     res= x/y
#     print(res)
# except:
#     print("Erro de exceção no codígo")
#     y= int(input("Digite um número interio maior que zero: "))
# finally:
#     res= x/y
#     print(res)




i = 0
soma= 0

while i < 10:
    try:
         x= int(input("Digite um número: "))
         soma+=x
         i+=1
    except:
        print("Valor Inválido!Tente novamente!!")


print(soma)