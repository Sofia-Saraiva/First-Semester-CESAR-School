cont = 0
with open('qp4.txt', 'r') as arquivo:
  f = arquivo.readlines()
  for i in range(len(f)):
    if int(f[i]) > int(f[i - 1]):
      cont += 1

print(cont)