numero = int(input("Informe um número inteiro: "))

inicio = 1
resultado = ''
letra = 'A'

while inicio <= numero:
   resultado = resultado + letra
   if inicio % 3 == 0:
       if letra == "A":
           letra = "B"
       elif letra == "B":
           letra = "C"
       elif letra == "C":
           letra = "A"

   inicio = inicio + 1

print(resultado)
