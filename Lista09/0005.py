def somaListas(lista1, lista2):
   soma_lista1 = 0
   soma_lista2 = 0
   for numero in lista1:
       soma_lista1 += sum(lista1)
   for numero in lista2:
       soma_lista2 += sum(lista2)
   if soma_lista1 > soma_lista2:
       resultado = True
   else:
       resultado = False
   return resultado


print(somaListas([10, 20, 30, 40, 50], [1, 8, 9, 5, 10]))
