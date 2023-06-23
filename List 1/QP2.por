programa {
  funcao inicio() {
    real km, dias, preco

    escreva("Quantidade de Km percorridos: ")
    leia(km)
    escreva("Quantidade de dias pelo qual ele foi alugado: ")
    leia(dias)

    preco = 90 * dias + 0.2 * km
    escreva("Preço total a pagar: R$", preco)

  }
}
