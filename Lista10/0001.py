from random import randrange

def numerosAleatorios(numero):
   lista_numeros_aleatorios = []
   for i in range(numero):
       lista_numeros_aleatorios.append(randrange(100))
   return lista_numeros_aleatorios

numeros = int(input("Informe a quantidade de números aleatórios: "))
print(numerosAleatorios(numeros))
