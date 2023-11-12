from funcoes.primos import ePrimo

def primosLista(lista):
   numeros_primos = []
   for numero in lista:
       if ePrimo(numero):
           numeros_primos.append(numero)
   return numeros_primos


print(primosLista([1,3,7,9,11,15,19,60]))