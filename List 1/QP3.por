programa {
  funcao inicio() {
    real n1, n2, n3, media
    cadeia nome

    escreva("Nome do aluno: ")
    leia(nome)
    escreva("Nota 1: ")
    leia(n1)
    escreva("Nota 2: ")
    leia(n2)
    escreva("Nota 3: ")
    leia(n3)

    media = (n1 * 2 + n2 * 3 + n3 * 5) / 10

    se (media <= 4.9) {
      escreva("Status: reprovado")
    }
    senao se (media >= 5 e media <= 6.9) {
      escreva("Status: recuperação")
    }
    senao se (media >= 7) {
      escreva("Status: aprovado")
    }
  }
}
