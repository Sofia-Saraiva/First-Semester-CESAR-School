linha = int(input("Digite a linha que a torre se encontra: "))
coluna = int(input("Digite a coluna que a torre se encontra: "))

print("Movimentos possíveis:")
print("  1 2 3 4 5 6 7 8")
for i in range(1, 9):
    print(i, end =' ')
    for j in range(1, 9):
        if linha != i and coluna != j:
            print(f"-", end=' ')
        else:
            print(f"x", end=' ')
    print()

