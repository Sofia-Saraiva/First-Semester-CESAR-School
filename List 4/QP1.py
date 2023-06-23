a = []
b = []
c = []

for i in range(5):
  a.append(int(input("A: ")))
  b.append(int(input("B: ")))

c = a + b

par = 0
soma_impar = 0
cont_impar = 0

for i in c:
  if i % 2 == 0:
    par += i
  else:
    soma_impar += i
    cont_impar += 1
    
media = soma_impar / cont_impar
menor = min(c)
print(f"Soma dos números pares do vetor C: {par}")
print(f"Média dos números ímpares do vetor C: {media}")
print(f"Menor valor do vetor C: {menor}")