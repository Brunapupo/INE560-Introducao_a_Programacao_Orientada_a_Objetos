def intervalo(inicio, fim, numero):
   if inicio <= numero <= fim:
       resultado = True
   else:
       resultado = False
   return resultado


inicio = int(input("Informe o inicio: "))
fim = int(input("Informe o fim: "))
numero = int(input("Informe um número: "))

print(intervalo(inicio,fim, numero))
