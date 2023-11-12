def inputMatriz(qtLinhas):
   r = []
   for l in range(qtLinhas):
       r.append([int(ent) for ent in input().split()])
   return r

def diagonal_principal(m):
   ind = 0
   diagonal = []
   while ind < len(m):
       diagonal.append(m[ind][ind])
       ind += 1
   return diagonal

def matriz_multiplicada_pela_diagonal(m):
   resultado = []
   diagonal_elementos = diagonal_principal(m)
   linha = 0
   mult = 0
   while linha < len(m):
       lista = []
       diagonal = diagonal_elementos[linha]
       col = 0
       while col < len(m[linha]):
           mult = diagonal * m[linha][col]
           lista.append(mult)
           col += 1
       linha += 1
       resultado.append(lista)
   return resultado

linhas = int(input())
matriz_entrada = inputMatriz(linhas)
nova_matriz = matriz_multiplicada_pela_diagonal(matriz_entrada)

for linha in nova_matriz:
   for coluna in linha:
       print(coluna, end=' ')
   print()
