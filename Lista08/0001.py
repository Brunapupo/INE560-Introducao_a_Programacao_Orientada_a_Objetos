def fatorial(numero):
   resultado = 1
   cont = 1
   while cont <= numero:
       resultado *= cont
       cont += 1
   return resultado

num = int(input())
print(f"{fatorial(num)}")