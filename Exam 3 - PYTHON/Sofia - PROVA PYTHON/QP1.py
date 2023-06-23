lista = []

while True:
    try:
        for i in range(5):
            user = input("Digite seu nome de usuário: ")
            foto1 = int(input("Digite o número de curtidas da foto 1: "))
            foto2 = int(input("Digite o número de curtidas da foto 2: "))
            foto3 = int(input("Digite o número de curtidas da foto 3: "))
            lista.append({'user': user, 'curtidas': [foto1,foto2,foto3]})
        break
    except ValueError:
        print("Digite um número válido.")
    #lista.append({'user': user, 'curtidas': [foto1,foto2,foto3]})
        

maior = 0
for dict in lista:
    media = sum(dict['curtidas']) / 3
    if media > maior:
        maior = media
        maiorUser = dict['user']
    print(f"User: {dict['user'].title()} - Média: {media:.2f}")

print(f"Quem obteve a maior média: {maiorUser.title()}")
    


