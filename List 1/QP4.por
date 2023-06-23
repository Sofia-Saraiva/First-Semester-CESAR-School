programa {
  funcao inicio() {
    real altura, peso, imc

    escreva("Altura: ")
    leia(altura)
    escreva("Peso: ")
    leia(peso)

    imc = peso / (altura * altura)

    se (imc < 18.5) {
      escreva("Abaixo do peso")
    }
    senao se (imc >= 18.5 e imc < 25) {
      escreva("Peso ideal")
    }
    senao se (imc >= 25 e imc < 30) {
      escreva("Sobrepeso")
    }
    senao se (imc > 40) {
      escreva("Obesidade mórbida")
    }
  }
}
