frase = input("Digite uma frase: ")

palavras = frase.split()
print(f"Quantidade de palavras: {len(palavras)}")

if frase.count('e') > 0:
    print(f"Quantidade de letras 'e': {frase.count('e')}")
else:
    print(f"Quantidade de letras 'e': Não existe.")
    
print(f"Terceira palavra da frase: {palavras[2]}")