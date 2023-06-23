matriz = [[],[],[]]
soma = 0

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f"Insira os dados da unidade {i+1}: ")))

for i in range(3):
    for j in range(3):
        if i == 0:
            soma += matriz[0][j]
            
        print(f"[{matriz[i][j]:^4}]", end='')
    print()

media = soma / 3
print(f"Média das notas da unidade 1: {media}")