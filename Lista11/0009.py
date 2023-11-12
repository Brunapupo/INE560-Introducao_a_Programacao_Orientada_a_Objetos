def verifica_nulos(matriz):
   lista_nulos = []
   for linha in range(len(matriz)):
       for coluna in range(len(matriz[linha])):
           if matriz[linha][coluna] == ' ':
              lista_nulos.append([f" O elemento nulo está na linha {linha}, e na coluna {coluna}"])

   return lista_nulos



m = [
  [333, ' ', 7, 4],
  [2, 5, 8, 3,],
  [5, ' ', 5, 8],
  [3, 8, 9, 3]
  ]

print(verifica_nulos(m))
