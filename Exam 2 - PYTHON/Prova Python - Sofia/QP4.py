votos = []
maior = 0
maiorvotos = 0
maiorporcent = 0
while True:
    voto = int(input("Vote: "))
    if voto >= 1 and voto <= 6:
        votos.append(voto)
    elif voto == 0:
        break
    else:
        print("Voto inválido")

print(f"Resultado da votação:\n - Foram computados {len(votos)} votos")
for i in range(1, 7):
    porcentagem = votos.count(i) / len(votos)
    print(f"Jogador {i} teve {votos.count(i)} votos. %: {porcentagem*100}")
    if votos.count(i) > maior:
        maior = i
        maiorvotos = votos.count(i)
        maiorporcent = porcentagem


print(f"O melhor jogador foi o número {maior}, com {maiorvotos} votos, correspondendo a {maiorporcent*100:3f}% do total dos votos")