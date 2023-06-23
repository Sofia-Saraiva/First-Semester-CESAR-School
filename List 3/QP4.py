time1 = input("Nome do time 1: ")
gol1 = int(input("Gols do time 1: "))
time2 = input("Nome do time 2: ")
gol2 = int(input("Gols do time 2: "))

if gol1 > gol2:
  print(f"{time1} venceu!")
elif gol1 == gol2:
  print("Empate!")
else:
  print(f"{time2} venceu!")