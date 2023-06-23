nome = input("Qual seu nome? ")
idade = int(input("Quantos anos você tem? "))
doenca = input("Possui alguma doença contagiosa? [S/N] ")

if idade >= 65:
  print("Atendimento com prioridade")
  if doenca == 'S':
    print("Sala amarela")
  else:
    print("Sala branca")
else:
  print("Atendimento sem prioridade")
  if doenca == 'S':
    print("Sala amarela")
  else:
    print("Sala branca")