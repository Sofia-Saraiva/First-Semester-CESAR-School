matriz = [[], [], []]

for linha in range(3):
  for coluna in range(3):
    matriz[linha].append(float(input(f"Digite [{linha}][{coluna}]: ")))

final = []
for linha in range(3):
  soma = 0
  for coluna in range(3):
    soma += matriz[coluna][linha]
  final.append(soma)

print(final)