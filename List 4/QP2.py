estagiarios = []

for i in range(3):
  salario = float(input(f"Salário do {i+1}º estagiário: "))
  transporte = float(input(f"Vale-transporte do {i+1}º estagiário: "))
  alimentacao = float(input(f"Vale-alimentação do {i+1}ª estagiário: "))
  estagiarios.append([salario, transporte, alimentacao])

print("Salário | Vale-transporte | Vale-alimentação")
print("--------------------------------------------")
for linha in range(3):
  for coluna in range(3):
    print(f"R${estagiarios[linha][coluna]:^7}", end=' ')
  print()

media = sum([i[0] for i in estagiarios]) / 3
total_vt = sum([i[1] for i in estagiarios])
print(f"Média salarial: {media}")
print(f"Total em vale-transporte: {total_vt}")