def main():
  nome = input("Digite o nome do arquivo: ")
  arquivo(nome)
  ordenados = []
  try:
    with open(nome, 'r') as f:
      linhas = f.readlines()
      ordenados = sorted(linhas)
  except IOError:
    print("Arquivo não encontrado.")

  with open('ordenado.txt', 'w') as newf:
    for i in ordenados:
      newf.writelines(i)
    
  
def arquivo(nome_arquivo):
  with open(nome_arquivo, 'w') as f:
    for i in range(6):
      nomes = input("Digite nome: ").title()
      nomes= f"{nomes}\n"
      f.writelines(nomes)

if __name__ == "__main__":
  main()