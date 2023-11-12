def coluna_eh_positivo(matriz, coluna):
   resultado = False
   for linha in matriz:
       if linha[coluna] > 0:
           resultado = True
   return resultado


def linha_eh_positivo(linha):
   resultado = False
   for i in linha:
       if i > 0:
           resultado = True
   return resultado

def valores_negativos(matriz):
   lista_negativos = []
   for i in range(len(matriz)):
       if not linha_eh_positivo(matriz[i]):
           lista_negativos.append(f" A linha {i} possui apenas valores negativos")
       if not coluna_eh_positivo(matriz, i):
           lista_negativos.append(f" A coluna {i} possui apenas valores negativos")

   return lista_negativos



m = [
  [-333, -99, -7, -9],
  [444, -55, 8, 3],
  [555, -45, 5, 8],
  [101, -77, 9, 3]
]

print(valores_negativos(m))
