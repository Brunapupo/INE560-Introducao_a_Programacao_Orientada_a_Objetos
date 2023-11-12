def somaLista(lista):
   soma_lista_pares = []
   for numero in lista:
       if numero % 2 == 0:
           soma_lista_pares.append(numero)
   return soma_lista_pares

print(somaLista([1,2,6,8,12,23,17,7,10,22]))