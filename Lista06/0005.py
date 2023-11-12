num = int(input("Informe o número que deseja saber o múltiplo: "))
total_multiplo = int(input("Informe os múltiplos: "))

x = 1
resultado = 0
while x <= total_multiplo:
   resultado = x * num
   print(resultado)

   x += 1