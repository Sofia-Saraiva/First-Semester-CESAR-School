programa
{
	
	funcao inicio()
	{
		inteiro x, y

		escreva("X: ")
		leia(x)
		escreva("Y: ")
		leia(y)

		se (x > 0 e y > 0) {
			escreva("primeiro")
		}
		senao se (x < 0 e y > 0) {
			escreva("segundo")
		}
		senao se (x < 0 e y < 0) {
			escreva("terceiro")
		}
		senao se (x > 0 e y < 0) {
			escreva("quarto")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 323; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */