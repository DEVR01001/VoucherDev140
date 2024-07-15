nome_completo= input("Digite seu nome completo: ")
cargo= input("Qual cargo está concorendo: ")
email= input("Digite seu e-mail: ")
idade= int(input("Digite sua idade: "))
if( idade >=18):
    print("Parabéns você passou para a próxima fase!!")
    cursoqualificação= input("Digite (S) se você possui algum curso de qualificaação na área ou (N) se não possuir: ")
    if( cursoqualificação == "S"):
        print("Parabéns você passou para a próxima fase!!")
        nota= float(input("Digite sua nota da prova: "))
        if(nota > 7):
            print("Parabéns você passou para a próxima fase!!")
        else:
            ## nvio de e-mail ##
            print("Obrigado por sua participação!!.")
    else:
        print("Obrigado por sua participação!!")
else:
    print("Obrigado por sua participação!!")
 