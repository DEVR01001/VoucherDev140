#### Utilize a fórmula de Euclides para Calcular a distância entre dois pontos: ####
#### Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponde ####
#### Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, ####
#### respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos ####
#### devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo ####
#### plano. Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima ####
#### longe na saída. Caso o contrário, quando a distância for menor que 10, imprima perto ####
import math
num1x = float(input("Digite o primeiro numero na linha x: "))
num1y = float(input("Digite o segundo numero na linha y: "))
num2x = float(input("Digite o terceiro numero na linha x: "))
num2y = float(input("Digite o quarto numero na linha y: "))
distanciaentreosdoispontos= pow((num1x-num2x), 2) + pow((num1y-num2y), 2)
raiz= math.sqrt(distanciaentreosdoispontos)
print(f"A distancia entre os dois pontos é {distanciaentreosdoispontos}")
if raiz >= 10: 
    print("Longe na sáida")
else:
    print("Perto da saída")