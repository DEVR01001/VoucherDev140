programa {
  funcao inicio() {
    real saque, conta, sobra
    escreva("Bem vindo ao saque teu dinheiro!! \n")
    escreva("Digite o quanto voc� quer sacar: ")
    leia(saque)
    conta = 1000.00
    se (saque < 1000){
      escreva("Voc� possui saldo!! \n")
      escreva("\nVoce retirou: ", saque, "$")
      sobra= 1000 - saque
      escreva("\nVoc� possui na sua conta restantes: ", sobra, "$")
    }
    senao {
      escreva("Voc� n�o possui  saldo!! \n")
      escreva("Voce possui ", conta, "$ de saldo")

    }

  }
}
