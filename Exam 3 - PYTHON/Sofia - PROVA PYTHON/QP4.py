def escrever(arquivo):
    while True:
        try:
            nomes = []
            idades = []
            nome = input("Digite um nome: ")
            if nome == 'SAIR':
                break
            nomes.append(nome)
            idades.append(int(input("Digite uma idade: ")))
            with open(arquivo, 'a') as file:
                for i in range(len(nomes)):
                    file.write(f"{nomes[i]},")
                    idades[i] = f"{idades[i]}"
                    file.write(f"{idades[i]}\n")
        except ValueError:
            print("A idade deve ser númerica.")
        except TypeError:
            print("Função write só aceita string")



def ler(arquivo):
    try:
        repetido = []
        with open(arquivo, 'r') as file:
            f = file.readlines()
            print(f)
            for linha in f:
                print(linha.rstrip('\n'))
                if f.count(linha.lower()) > 1:
                    repetido.append(linha)
            print(repetido)
                
    except FileNotFoundError:
        print("Arquivo não existe.")

escrever('arquivo.txt')
ler('arquivo.txt')

