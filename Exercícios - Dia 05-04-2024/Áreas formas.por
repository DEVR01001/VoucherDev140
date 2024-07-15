programa {
  funcao inicio() {
    inteiro baset, baser, alturat, alturar, lado, a, b 
    real c, r, d
    escreva("BOM DIA!!  \n")
    escreva("Vamos calcular a área de um quadrado, de um retângulo, de um triângulo e um circulo. \n")
     escreva("\n")
    escreva("Primeiro, digite o lado(l) do quadrado: ")
    leia(lado)
    escreva("Calculando... \n")
     escreva("\n")
    escreva("Digite a base(b) do retângulo: ")
    leia(baser)
    escreva("Digite a altura(a) do retângulo: ")
    leia(alturar)
    escreva("Calculando... \n")
     escreva("\n")
    escreva ("Digite a base(b) do triângulo: ")
    leia(baset)
    escreva("Digite a altura(a) do triângulo: ")
    leia(alturat)
    escreva("Calculando... \n")
    escreva("\n")
    escreva("Digite o raio do circulo: ")
    leia(r)
    escreva("Calculando... \n")
     escreva("\n")
    a = lado*lado
    b = baser*alturar
    c = baset*alturat/2
    d = r*r*3.14
    escreva("O resultado da área do quadrado é: ", a,"\n")
    escreva("O resultado da área do retângulo é: ", b,"\n")
    escreva("O resultado da área do triângulo é: ", c,"\n")
    escreva("O resultado da área do circulo é: ", d, "\n")
    escreva("Obrigado por calcular em nosso código:) ")



  }
}
