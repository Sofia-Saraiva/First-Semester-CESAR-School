cont = 0
mais_rapido = 0
mais_novo = 3000
while True:
  carro = input("Gostaria de parar a leitura? [N] ")
  if carro == 'N':
    break
  ano = int(input("Ano do carro: "))
  velocidade = int(input("Velocidade do carro: "))
  cont+=1
  if velocidade > mais_rapido:
    mais_rapido = velocidade

  if ano < mais_novo:
    mais_novo = ano

print(f"Quantidade de carros: {cont}\nCarro mais veloz {mais_rapido}\nCarro mais novo: {mais_novo}")