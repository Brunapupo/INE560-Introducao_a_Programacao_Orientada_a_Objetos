from funcoes.primos import ePrimo

def primosLista(lista):
   numeros_primos = []
   for numero in lista:
       if ePrimo(numero):
           numeros_primos.append(numero)
   return numeros_primos


numeros = input("Informe os números: ")
numeros = numeros.split(',')
lista_numeros = []
for i in numeros:
   lista_numeros.append(int(i))

print(primosLista(lista_numeros))