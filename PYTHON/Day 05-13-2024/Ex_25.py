# Crie um programa que leia um número indeterminado de idades de indivíduos(pare 
# quando foir informada a indade 0), e calcule a indade média desse grupo.



soma= 0
i =0
while True:
    num =int(input("Digite um idade(digite 0 para finalizar e saber média): "))
    if num == 0:
        break
    elif num >0:    
        soma+=num
        i+=1
        media= soma/i
print(media)
