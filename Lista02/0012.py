quantidade_km = int(input("Informe a quantidade de km percorridos:"))
quantidade_dias = int(input("Informe a quantidade de dias do aluguel do carro:"))

km = quantidade_km * 0.15
dias = quantidade_dias * 60
soma = km + dias
print(f"{soma}")
