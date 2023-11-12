quantidade_dias = int(input("dias:"))
quantidade_horas = int(input("horas:"))
quantidade_minutos = int(input("minutos:"))
quantidade_segundos = float(input("segundos:"))

horas = quantidade_dias * 24
minutos = (horas + quantidade_horas) * 60
segundos =  (minutos + quantidade_minutos) * 60 + quantidade_segundos
print(f"Total em segundos: {segundos:.0f}s")

