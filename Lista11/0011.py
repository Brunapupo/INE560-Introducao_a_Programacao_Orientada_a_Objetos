def matriz_simetrica(matriz):
   lista_matriz_transposta = []

   for i in range(len(matriz)):
       lista = []
       for linha in matriz:
           lista.append(linha[i])
       lista_matriz_transposta.append(lista)


   return lista_matriz_transposta == matriz

m = [
   [3, 5, 6],
   [5, 2, 4],
   [6, 4, 8]
   ]

if(__name__ == "__main__"):
   print(matriz_simetrica(m))
   