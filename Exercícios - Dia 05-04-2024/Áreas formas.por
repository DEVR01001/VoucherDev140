programa {
  funcao inicio() {
    inteiro baset, baser, alturat, alturar, lado, a, b 
    real c, r, d
    escreva("BOM DIA!!  \n")
    escreva("Vamos calcular a �rea de um quadrado, de um ret�ngulo, de um tri�ngulo e um circulo. \n")
     escreva("\n")
    escreva("Primeiro, digite o lado(l) do quadrado: ")
    leia(lado)
    escreva("Calculando... \n")
     escreva("\n")
    escreva("Digite a base(b) do ret�ngulo: ")
    leia(baser)
    escreva("Digite a altura(a) do ret�ngulo: ")
    leia(alturar)
    escreva("Calculando... \n")
     escreva("\n")
    escreva ("Digite a base(b) do tri�ngulo: ")
    leia(baset)
    escreva("Digite a altura(a) do tri�ngulo: ")
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
    escreva("O resultado da �rea do quadrado �: ", a,"\n")
    escreva("O resultado da �rea do ret�ngulo �: ", b,"\n")
    escreva("O resultado da �rea do tri�ngulo �: ", c,"\n")
    escreva("O resultado da �rea do circulo �: ", d, "\n")
    escreva("Obrigado por calcular em nosso c�digo:) ")



  }
}
