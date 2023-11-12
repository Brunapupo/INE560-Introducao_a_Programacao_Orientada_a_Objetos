lado1 = abs(float(input("Informe o primeiro lado do triângulo: ")))
lado2 = abs(float(input("Informe o segundo lado do triângulo: ")))
lado3 = abs(float(input("Informe o terceiro lado do triângulo: ")))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
   print(f"Os valores informados são negativos, informe valores positivos. ")
else:
   if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
       if lado1 == lado2 == lado3:
           print("equilátero")
       elif lado1 != lado2 != lado3!= lado1:
           print("escaleno")
       elif lado1 == lado2 or lado2 == lado3:
           print("isósceles")
       else:
           print(f"Os valores não obedecem a condição de existência de um triângulo. ")
