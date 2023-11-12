from statistics import mode
from statistics import mean

def notasMedia(lista):
   for numero in lista:
       if numero < 0 or numero > 10:
           return None
   media_lista = mean(lista)
   moda_lista = mode(lista)
   return [media_lista, moda_lista]

print(notasMedia([8.00, 7.88, 9.00, 10.00]))