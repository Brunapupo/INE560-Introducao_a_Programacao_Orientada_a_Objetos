def MostraMatriz(m):
    for linha in m:
        for coluna in linha:
            print(f"{coluna}", end=' ')
        print()

def criaMatrizSequencial(m, n):
    ret = []
    for i in range(m):
        noval = list(range(i, i+n))
        ret.append(noval)
    return ret

m = criaMatrizSequencial(5, 5)
MostraMatriz(m)

m = [
   [5, 1, 2, 3],
   [2, 5, 3, 3],
   [5, 7, 5, 6],
   [3, 8, 9, 5]
   ]

resultado = True
l = 0
tam = len(m)
c = len(m) - 1
numinicial = m[l][c]
while l < tam:
    segunda_diagonal = m[l][c]
    if numinicial != segunda_diagonal:
        resultado = False
    l += 1
    c -= 1

print(resultado)
