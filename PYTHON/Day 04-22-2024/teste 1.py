a= int(input("Digite um numero: "))
b= int(input("Digite outro numero: "))
c= a*b
if (c > 0):
    if ( c > 50):
        print("Tudo ok par decolar!!!")
    else:
        print("Tanque principal vazio, voando com combustivél reserva!!")
else:
    if (c < 0):
        print("Foguete não tem piloto, mas há outros foguetes disponíveis!!")
    
