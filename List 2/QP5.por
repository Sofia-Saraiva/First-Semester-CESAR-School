programa {
  funcao inicio() {
    inteiro numero, soma=0

    faca {
      escreva("Digite um número: ")
      leia(numero)
      se (numero != 1111) {
        soma = soma + numero
      }
    } enquanto (numero != 1111)

    escreva("Somatório: ", soma)
  }
}
