cateto1 = int(input("Informe o primeiro cateto:"))
cateto2 = int(input("Informe o segundo cateto:"))

if cateto1 <= 0 and cateto2 <= 0:
   print("Informe números positivos.")
else:
   hipotenusa =  ((cateto1 ** 2 ) + (cateto2 ** 2)) ** 0.5
   print(hipotenusa)