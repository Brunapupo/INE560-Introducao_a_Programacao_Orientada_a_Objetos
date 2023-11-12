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


m = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8]
    ]

resultado = matriz_multiplicada_pela_diagonal(m)


for r in resultado:
    print(r)