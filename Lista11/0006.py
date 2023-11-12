def numero_na_matriz(matriz, numero):
   resultado = False
   for i in matriz:
       for j in i:
           if numero in i:
               resultado = True
           else:
               resultado = False
   return resultado


m = [
  [0, 1, 2, 3],
  [2, 5, 3, 3],
  [5, 9, 5, 6],
  [3, 8, 9, 10]
  ]

print(numero_na_matriz(m, 333))

def numero_na_matriz(matriz, numero):
   resultado = False
   linha = 0
   qt_linha = len(matriz)
   while linha < qt_linha:
       col = 0
       qt_col = len(matriz[linha])
       while col < qt_col:
           if numero == matriz[linha][col]:
               resultado = True
           else:
               resultado = False
           col += 1
       linha += 1
   return resultado

m = [
  [0, 1, 2, 3],
  [2, 5, 3, 3],
  [5, 9, 5, 6],
  [3, 8, 9, 333]
  ]

print(numero_na_matriz(m, 333))