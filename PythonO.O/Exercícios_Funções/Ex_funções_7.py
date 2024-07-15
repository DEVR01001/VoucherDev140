# Crie uma função de um programa de teste para o cálculo do volume de uma esfera. Sendo que o 
# raio é passado por parâmetro?
# V = 4/3 ∗ π ∗ R3


def VolumeEsfera(raio):
    V= ((4/3) * 3.14) * (raio**3)
    print(f"O volume da esfera de raio{raio} é {V}")
    return V

raio= float(input("Digite o número do raio da esfera: "))

VolumeEsfera(raio)