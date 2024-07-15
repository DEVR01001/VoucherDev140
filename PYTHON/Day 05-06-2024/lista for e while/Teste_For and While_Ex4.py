# Faça um algoritmo que receba o número de avaliações do estudante que será(ultilizado como contador), 
# após as notas e apresente a média do estudante.


# while 
n = int(input("Digite o número de valiações: "))

i= 0
soma= 0
while i < n:
    soma += int(input("Digite a nota das avaliações: "))
    i += 1
media = soma / n
print( media)

# while lista
numero_notas= int(input("Digite o número de avliações: "))
contador= 0 
notas = []

while contador < numero_notas:
    notas.append(int(input("Digite a nota das avaliações: ")))
    contador = contador + 1
    media = sum(notas)/len(notas) 
print(f"A média é {media}")