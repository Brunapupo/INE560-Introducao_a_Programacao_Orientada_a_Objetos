angulo1 = int(input("Informe o primeiro ângulo do triângulo: "))
angulo2 = int(input("Informe o segundo ângulo do triângulo: "))
angulo3 = int(input("Informe o terceiro ângulo do triângulo: "))

if angulo1 + angulo2 + angulo3 > 180:
   print("A soma dos ângulos ultrapassaram 180º.")
else:
   if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
       print("Triângulo Acutângulo: possui todos os ângulos com medidas menores de 90o")
   elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
       print("Triângulo Retângulo: possui um ângulo com medida igual a 90o")
   else:
       print("Triângulo Obtusângulo: possui um ângulo obtuso, maior que 90o")
