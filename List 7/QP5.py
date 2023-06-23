def main():
  nome = input("Digite o nome do arquivo: ")
  nome_arquivo(nome)
  alterar(nome)
  

def nome_arquivo(nome):
  with open(nome, 'w') as f:
    for i in range(6):
      nome_completo = input("Digite nome e sobrenome: ").title()
      nome_completo = f"{nome_completo}\n"
      f.writelines(nome_completo)


def alterar(nome):
  with open(nome, 'r') as f:
    linhas = f.readlines()
    for i in range(len(linhas)):
      alterar = input(f"Deseja alterar {linhas[i]}? [Sim]").lower()
      if alterar == 'sim':
        novo = input("Digite nome e sobrenome: ").title()
        linhas[i] = f"{novo}\n"
        with open(nome, 'w') as f:
          f.writelines(linhas)
        
      
if __name__== '__main__':
  main()