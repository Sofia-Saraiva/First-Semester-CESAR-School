programa {
  funcao inicio() {
    real largura, altura, area, tinta

    escreva("Largura da parede: ")
    leia(largura)
    escreva("Altura da parede: ")
    leia(altura)

    area = largura * altura
    tinta = area / 2
    escreva("�rea a ser pintada: ", area, "m2", 
            "\nQuantidade de tinta necess�ria: ", tinta, " litros")

  }
}
