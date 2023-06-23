programa {
  funcao inicio() {
    real km, preco

    escreva("Quantos Km deseja percorrer? ")
    leia(km)

    se (km > 200) {
      preco = 0.45 * km
      escreva(preco)
    }
    senao {
      preco = 0.5 * km
      escreva(preco)
    }
  }
}
