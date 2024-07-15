# Crie um pograma que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.



num = 0
soma= 0


while  num < 1000:
    if num % 3 == 0 or num % 5==0:
        soma+=num
    num+=1

print(f"A soma dos multiplos de 3 e 5 é {soma}")