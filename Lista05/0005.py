medida = input("Informe uma unidade de medida: ")
temperatura = int(input("Informe a temperatura: "))

if medida == 'celsius':  # fahrenheit
  conversao = (temperatura * 9 / 5) + 32
  print(conversao)
  conversao = (temperatura + 273.15)
  print(conversao)
elif medida == 'fahrenheit':  # celsius
  conversao = (temperatura - 32) * 5 / 9
  print(conversao)
  conversao = (temperatura - 32) * 5/9 + 273.15
  print(conversao)
elif medida == 'kelvin':
  conversao = (temperatura - 273.15)
  print(conversao)
  conversao = (temperatura - 273.15) * 9/5 + 32
  print(conversao)
