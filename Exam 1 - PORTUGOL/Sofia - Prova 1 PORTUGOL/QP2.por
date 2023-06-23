programa
{
	
	funcao inicio()
	{
		inteiro area

		escreva("Digite a área do terreno: ")
		leia(area)

		se (area < 100) {
			escreva("Classificação: TERRENO POPULAR")
		}
		senao se (area >= 100 e area <= 500) {
			escreva("Classificação: TERRENO MASTER")
		}
		senao {
			escreva("Classificação: TERRENO VIP")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 314; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */