
programa {
  funcao inicio() {
    
        inteiro estq, sant, ent, sd 
        escreva("Bem vindo ao calcule o estoque atual de um produto \n")
        escreva("Digite o numero do estoque do produto do seu  ultimo m�s: ")
        leia(sant)
        escreva("Digite a quantidade de produto que foi comprada este m�s: ")
        leia(ent)
        escreva("Coloque a quantidade vendida e ultilizada total desse produto: ")
        leia(sd)
        estq = (sant+ent)-sd
        escreva("\nO estoque atual do porduto � ", estq)
        escreva("\nObrigado por ultilizar nossos calculos:)")


  }
}
