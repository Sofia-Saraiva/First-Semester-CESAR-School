lista = []
desc = []

n = int(input("Quantos números você deseja digitar? "))
for i in range(n):
    lista.append(int(input("Digite o número: ")))

for i in range(len(lista)):
    desc.append(max(lista))
    lista.remove(max(lista))

print(desc)

