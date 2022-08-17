#considerando o início do dia como 0.

horasUsuario = int(input("Para saber o total de minutos e segundos que já se passaram desde o início do dia, digite qual é a hora: "))

minutosUsuario = int(input("Agora digite os minutos: "))

segundosUsuario = int(input("Por fim, digite os segundos: "))

totalSegundos = horasUsuario * 3600 + minutosUsuario * 60 + segundosUsuario

totalMinutos = horasUsuario * 60 + minutosUsuario + (segundosUsuario / 60)

print("O total de segundos é de: ", totalSegundos,"s")

print("E o total de minutos é de : ", totalMinutos,"m")