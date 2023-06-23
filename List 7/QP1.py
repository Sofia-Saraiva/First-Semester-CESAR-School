numeros = []
maior = 0
menor = 0
igual = 0

while True:
  try:
    for i in range(10):
      n = int(input("Digite: "))
      numeros.append(n)
    break
  except ValueError:
    print("Digite um número.")


for i in numeros:
  if i > numeros[0]:
    maior += 1
  elif i < numeros[0]:
    menor += 1
  else:
    igual += 1

print(f"Maiores que {numeros[0]}: {maior}")
print(f"Menores que {numeros[0]}: {menor}")
print(f"Iguais que {numeros[0]}: {igual}")