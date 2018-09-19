segundos = int(input("Insira o tempo em segundos: "))
segrestantes = segundos%60
minutos = segundos//60
minrestantes = minutos%60
horas = minutos//60
print("\n Valor em horas: ", horas, " horas,", minrestantes, " minutos e ", segrestantes, " segundos.")
