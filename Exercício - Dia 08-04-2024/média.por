programa {
  funcao inicio() {
    
          inteiro n1, n2, media
          escreva("Bem vindo ao programa de calculo da m�dia final!!\n")
          escreva("Digite a nota da primeira prova: \n")
          leia(n1)
          escreva("Digite a nota da segunda prova: \n")
          leia(n2)
          media = n1+n2/2
          se ( media >= 7){
            escreva("A nota da sua primeira prova foi: ", n1)
            escreva("A nota da sua segunda prova foi: ", n2)
            escreva("Sua m�dia foi: ", media)
            escreva("\nVoc� foi aprovado!!!")
          }
          senao{
            escreva("\nA nota da sua primeira prova foi: ", n1)
            escreva("\nA nota da sua segunda prova foi: ", n2)
            escreva("\nSua m�dia foi: ", media)
            escreva("\nVoc� n�o foi aprovado!!!")
          }
          escreva("\nObrigado por usar nosso calculador de m�dia!!! Volte sempre.")




  }
}
