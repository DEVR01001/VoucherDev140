#### Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, ####
#### utilizando as seguintes formulas (onde h corresponde à altura): ####
#### • Homens: (72.7∗ h)−58 ####
#### • Mulheres: (62,1∗ h)−44,7 ####


altura= float(input("Digite sua alatura em metros: "))
sexo= str(input("Digite seu sexo. Use (M) para masculino e (F) para feminino: "))


if( sexo == "M"):
    homem= (72.7*altura)-58
    print(f"Seu peso ideal é {homem} Kg")
elif( sexo == "F"):
    mulher= (62.1*altura)-44.7
    print(f"Seu peso ideal é {mulher} Kg")