programa {
  funcao inicio() {
        real area, base, altura, preco

        escreva("Bem, vindo ao calucule a área do tereno \n")
        escreva("Digite a base do tereno: ")
        leia(base)
        escreva("Digite a altura do tereno: ")
        leia(altura)
        area = base*altura
        preco = area*750.00
        escreva("Calculando... \n")
        escreva("\n")
        escreva("O preço desse terreno é: $", preco, ",00 reais. \n")
        escreva("\n")
        escreva("Obrigado por ultilizar o programa :)")


  }
}
