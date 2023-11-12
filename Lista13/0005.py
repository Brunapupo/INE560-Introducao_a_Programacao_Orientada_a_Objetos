def verifica_diagonal_abaixo_valor_zero(m):
    resultado = []
    diagonal = 1
    while diagonal <= len(m) - 1:
        linha = diagonal
        coluna = 0
        lista = []
        while linha <= len(m) - 1:
            elemento = m[linha][coluna]
            lista.append(elemento)
            linha += 1
            coluna += 1
        diagonal += 1


        resultado.append(lista)
    resultado_com_zeros = []
    for i in resultado:
        if 0 in i:
            resultado_com_zeros.append(i)
    return resultado_com_zeros


def verifica_diagonal_acima_valor_zero(m):
    resultado = []
    diagonal = 1
    while diagonal <= len(m) - 1:
        linha = 0
        coluna = diagonal
        lista = []
        while coluna <= len(m) - 1:
            elemento = m[linha][coluna]
            lista.append(elemento)
            linha += 1
            coluna += 1
        diagonal += 1
        resultado.append(lista)
    resultado_com_zeros = []
    for i in resultado:
        if 0 in i:
            resultado_com_zeros.append(i)
    return resultado_com_zeros

def verifica_diagonais_acima_abaixo(m):
    check_acima = verifica_diagonal_acima_valor_zero(m)
    check_abaixo = verifica_diagonal_abaixo_valor_zero(m)
    return check_acima, check_abaixo


m = [[1, 0, 7, 4],
     [3, 8, 3, 5],
     [0, 2, 2, 9],
     [5, 2, 1, 6]]

print(verifica_diagonais_acima_abaixo(m))
