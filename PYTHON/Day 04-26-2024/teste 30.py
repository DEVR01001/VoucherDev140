#### Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. ####
#### Escreva uma mensagem de erro se a opção for inválida. ####
#### Escolha a opção:####
#### 1- Soma de 2 números. ####
#### 2- Diferença entre 2 números (maior pelo menor).####
#### 3- Produto entre 2 números. ####
#### 4- Divisão entre 2 números (o denominador não pode ser zero) ####

num1= float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))

escolha= input("Escolha entre: \n(soma)\n(diferença) maior pelo menor \n(produto)  \n(divisão) enominador não pode ser zero): ")

if( escolha == "soma"):
    soma= num1+num2
    print(f"A diferença entre os dois número é de {soma}")
elif( escolha == "diferença"):
    diferença= num1-num2
    print(f"O produto entre os dois número é de {diferença}")
elif( escolha == "soma"):
    produto= num1*num2
    print(f"A soma entre os dois número é de {produto}")
elif( escolha == "soma"):
    divisao= num1/num2
    print(f"A soma entre os dois número é de {divisao}")

