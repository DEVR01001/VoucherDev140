# 1 - Escreva um programa Python que solicite ao usuário que insira um inteiro e gere uma exceção ValueError se a entrada não for um inteiro válido.



# try:    
#         num=int(input(F"Digite um número inteiro: "))
#         print(f"Numero inteiro")

# except:
#     print(f"Numero não inteiro")




# 2 - Escreva um programa Python que solicite ao usuário que insira dois números e gere uma exceção TypeError se as entradas não forem numéricas.


# try:
#       num1=(input("Digite um número: "))
#       num2=(input("Digite outro número: "))
#       if not isinstance(num1,float):
#             a= float(num1)
#             b= float(num2)
#             print(f"{a} e {b}")
#       elif isinstance(num1,float):
#             a= float(num1)
#             b= float(num2)
#             print(f"{a} e {b}")

#       elif not isinstance(num2,float):
#             a= float(num1)
#             b= float(num2)
#             print(f"{a} e {b}")
#       elif isinstance(num2,float):
#             a= float(num1)
#             b= float(num2)
#             print(f"{a} e {b}")

# except:
#       print(f"Você digitou letras!")
      

# 3 - Crie uma função para realizar o saque de conta corrente. Uma exceção é lançada sempre que o saldo da conta for inferior ao valor sacado.



# a = False

# while a == False:
# #     saque= float(input("Digite o valor a sacar: "))
# #     saldo_conta = 1000
try:
      a = False

      while a == False:
            saque= float(input("Digite o valor a sacar: "))
            saldo_conta = 1000
            if saque < saldo_conta:
                  calculo= saldo_conta - saque
                  print(f"O saque de {saque}R$ foi feito com Sucesso!!!")
                  print(f"Saldo atual de {calculo}R$")
                  a = True
      
except:
      print(f"Saldo insuficiente")
      a= True