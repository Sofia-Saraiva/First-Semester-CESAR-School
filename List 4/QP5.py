qntd = int(input("Quantidade de mouses: "))

cont_e = 0
cont_l = 0
cont_c = 0
cont_q = 0
for i in range(qntd):
  id = int(input("Número de identificação: "))
  esfera = input("Necessita de esfera?[S/N] ")
  if esfera == 'S':
    cont_e += 1
  limpeza = input("Necessita de limpeza?[S/N] ")
  if limpeza == 'S':
    cont_l += 1
  cabo = input("Necessita troca do cabo ou conector?[S/N] ")
  if cabo == 'S':
    cont_c += 1
  quebrado = input("Quebrado ou inutilizado?[S/N] ")
  if quebrado == 'S':
    cont_q += 1

print("Situação                          Quantidade      Percentual")
print(f"1- necessita da esfera             {cont_e}         {cont_e / qntd * 100}%")
print(f"2- necessita de limpeza            {cont_l}         {cont_l / qntd * 100}%")
print(f"3- necessita troca do cabo ou conector    {cont_c}               {cont_c / qntd * 100}%")
print(f"4- quebrado ou inutilizado         {cont_q}         {cont_q / qntd * 100}%")