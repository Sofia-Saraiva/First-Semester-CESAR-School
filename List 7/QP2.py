valido = []
invalido = []

with open('ips.txt', 'r') as arquivo:
  linhas = arquivo.readlines()

for i in linhas:
  i = i.rstrip()
  partes = i.split(".")
  partes = map(int, partes)
  if max(partes) < 255:
    valido.append(i)
  else:
    invalido.append(i)

print(f"Válidos: {valido}")
print(f"Inválidos: {invalido}")