programa {
  funcao inicio() {

    real peso, gravidade, pesoplaneta
    inteiro planeta

    escreva("Peso: ")
    leia(peso)
    escreva("Número do planeta [1 a 6]: ")
    leia(planeta)
    

    escolha(planeta){
      caso 1:
        gravidade = 0.37
        pesoplaneta = (peso / 10) * gravidade
        escreva("Peso no planeta: ", pesoplaneta)
        pare
      caso 2:
        gravidade = 0.88
        pesoplaneta = (peso / 10) * gravidade
        escreva("Peso no planeta: ", pesoplaneta)
        pare
      caso 3:
        gravidade = 0.38
        pesoplaneta = (peso / 10) * gravidade
        escreva("Peso no planeta: ", pesoplaneta)
        pare
      caso 4:
        gravidade = 2.64
        pesoplaneta = (peso / 10) * gravidade
        escreva("Peso no planeta: ", pesoplaneta)
        pare
      caso 5:
        gravidade = 1.15
        pesoplaneta = (peso / 10) * gravidade
        escreva("Peso no planeta: ", pesoplaneta)
        pare
      caso 6:
        gravidade = 1.17
        pesoplaneta = (peso / 10) * gravidade
        escreva("Peso no planeta: ", pesoplaneta)
        pare
      caso contrario:
        escreva("Número inválido")
    }
  }
}
