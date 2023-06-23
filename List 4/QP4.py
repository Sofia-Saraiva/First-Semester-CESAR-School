fib = [1, 1]
qntd = int(input("Digite um número: "))
for i in range(qntd - 2):
  soma = fib[len(fib) - 1] + fib[len(fib) - 2]
  fib.append(soma)
print(fib)