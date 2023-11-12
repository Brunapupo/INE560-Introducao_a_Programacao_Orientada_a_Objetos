from math import factorial

def listaFatorial(lista):
   lista_fatorial = []
   for numero in lista:
       lista_fatorial.append(factorial(numero))
   return lista_fatorial

print(listaFatorial([3, 4, 5, 6]))