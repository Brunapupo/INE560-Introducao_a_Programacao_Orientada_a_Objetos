def verificar_se_matriz_e_quadrado(matriz):
   linha = 0
   quadrada = True
   qtd_linha = len(matriz)
   while linha < qtd_linha:
       qtd_col = len(matriz[linha])

       if qtd_linha != qtd_col:
           quadrada = False

       linha += 1
   return quadrada

m = [
  [333, 1, 2, 4],
  [2, 5, 3, 3, 8, 9],
  [5, 9, 5, 6],
  [3, 8, 9, 3]
  ]

print(verificar_se_matriz_e_quadrado(m))