#### Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma ####
####taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa ####
#### em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço ####
#### final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado ####
#### não for válido, mostrar uma mensagem de erro. ####

valorporduto= float(input("Digite o valor do produto: "))
estado= input("Digite o estado (MG) Minas Gerais (SP) São Paulo (RJ) Rio de Janeiro, (MS) Mato Grosso do Sul: ")

if(estado == "MG"):
    calculo1= valorporduto*(7/100)
    produtofinalmg= valorporduto+calculo1
    print(f"O valor do produto para (MG) é de {produtofinalmg}")
elif(estado == "SP"):
    calculo2= valorporduto*(12/100)
    produtofinalsp= valorporduto+calculo2
    print(f"O valor do produto para (SP) é de {produtofinalsp}")
elif(estado == "RJ"):
    calculo3= valorporduto*(15/100)
    produtofinalrj= valorporduto+calculo3
    print(f"O valor do produto para (RJ) é de {produtofinalrj}")
elif(estado == "MS"):
    calculo4= valorporduto*(8/100)
    produtofinalms= valorporduto+calculo4
    print(f"O valor do produto para (MS) é de {produtofinalms}")
else:
    print("Estado digitado não está disponivel.")


