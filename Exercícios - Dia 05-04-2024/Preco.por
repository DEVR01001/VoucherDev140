programa {
  funcao inicio() {
        real area, base, altura, preco

        escreva("Bem, vindo ao calucule a �rea do tereno \n")
        escreva("Digite a base do tereno: ")
        leia(base)
        escreva("Digite a altura do tereno: ")
        leia(altura)
        area = base*altura
        preco = area*750.00
        escreva("Calculando... \n")
        escreva("\n")
        escreva("O pre�o desse terreno �: $", preco, ",00 reais. \n")
        escreva("\n")
        escreva("Obrigado por ultilizar o programa :)")


  }
}
