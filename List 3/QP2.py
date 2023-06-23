arvore = float(input("Valor da árvore: "))
quantidade = int(input("Quantidade de enfeite: "))
cont = 1
totalpreco = 0
while cont <= 3:
  preco = float(input("Preço unitário: "))
  preco += totalpreco
  cont+=1

total = (arvore + (quantidade * totalpreco)) / 21
print(f"Cada funcionário deve pagar R${total:.2f}")