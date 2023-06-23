programa {
  funcao inicio() {
    inteiro valor, valorinicial, valorfinal, cont, quantidade=0

    escreva("Montar a tabuada do: ")
    leia(valor)
    escreva("Começar por: ")
    leia(valorinicial)
    escreva("Terminar em: ")
    leia(valorfinal)

    quantidade = valorfinal - valorinicial 
    para (cont = 0; cont <= quantidade; cont++) {
      escreva(valor, " x ", valorinicial, " = ", valor * valorinicial, "\n")
      valorinicial = valorinicial + 1
    }
  }
}
