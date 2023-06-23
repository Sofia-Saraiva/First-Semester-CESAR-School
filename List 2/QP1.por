programa {
  funcao inicio() {
    
    caracter sexo
    inteiro cont, idade, media=0, soma_idade=0, homens=0, maisvelha=0, mais20=0

    para (cont = 1; cont <= 5; cont++) {
      escreva("Sexo[F/M]: ")
      leia(sexo)
      escreva("Idade: ")
      leia(idade)

      se (sexo == 'M') {
        homens++
      }

      se (sexo == 'F') {
        se (idade > maisvelha) {
          maisvelha = idade
        }

        se (idade > 20) {
          mais20++
        }
      }

      soma_idade = soma_idade + idade
    }

    media = soma_idade / 5
    escreva("Quantidade de homens: ", homens, "\nIdade da mulher mais velha: ", maisvelha, 
            "\nMédia de idade do grupo: ", media, "\nQuantidade de mulheres com mais de 20 anos: ", mais20)
  }
}
