def minas(bombas):
    resultado = []

    for i in range(len(bombas)): 
        bomba = 0
        if i == 1:
            bomba += 1

        if i != 0:
            if bombas[i - 1] == 1:
                bomba += 1
        if i != len(bombas) - 1:
            if bombas[i + 1] == 1:
                bomba += 1
        resultado.append(bomba)
    
    return resultado


bombas = []
n = int(input())
for i in range(n):
    bombas.append(int(input()))

print()
for i in minas(bombas):
    print(i)