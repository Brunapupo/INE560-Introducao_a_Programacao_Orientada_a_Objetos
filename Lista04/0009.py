a = float(input("Informe o primeiro lado: "))
b = float(input("Informe o segundo lado: "))
c = float(input("Informe o terceiro lado: "))

if a <=0 or b <= 0 or c <= 0:
   print(f"Informe um valor positivo. ")
else:
   if (a + b < c) or (a + c < b) or (b + c < a):
       print(f"Existe um Triângulo. ")
   else:
       print(f"Não existe um Triângulo. ")