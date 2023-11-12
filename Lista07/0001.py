inicio = int(input())
fim = int(input())

atual = inicio
while atual <= fim:
   mult = 1
   print(f"Tabuada do {atual}:")
   while mult <= 10:
       resultado = atual * mult
       print(f"{atual} x {mult} = {resultado}")
       mult = mult + 1
   atual = atual + 1
