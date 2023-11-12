def inputMatriz(qtLinhas):
    r = []
    for l in range(qtLinhas):
        r.append([int(ent) for ent in input().split()])
    return r


def diagonal_principal_soma(m):
    diagonal = []
    ind = 0
    soma = 0
    while ind < len(m):
        lista = []
        soma += (m[ind][ind])
        lista.append(soma)
        ind += 1
    diagonal.append(lista)
    return diagonal


def segunda_diagonal_soma(m):
    segunda_diagonal = []
    l = 0
    tam = len(m)
    c = len(m) - 1
    soma = 0
    while l < tam:
        lista = []
        soma += (m[l][c])
        lista.append(soma)
        l += 1
        c -= 1
    segunda_diagonal.append(lista)
    return segunda_diagonal


def pega_linha(m):
    lista = []
    linha = 0
    while linha < len(m):
        soma = []
        coluna = 0
        soma_linhas = 0
        while coluna < len(m[linha]):
            soma_linhas += m[linha][coluna]
            soma.append(soma_linhas)
            coluna += 1
        linha += 1
        lista.append(soma_linhas)
    return lista

def pega_coluna(m):
    lista = []
    for i in range(len(m)):
        soma = 0
        for linha in m:
            soma += linha[i]
        lista.append(soma)
    return lista

def verifica_igualdade_matriz(lista):
    tam_lista = len(lista)
    flag = True
    for i in range(1, tam_lista):
        if lista[i] != lista[i-1]:
            return False
    return flag


linhas = int(input())
matriz_entrada = inputMatriz(linhas)

diagonal = diagonal_principal_soma(matriz_entrada)
segundaDiagonal = segunda_diagonal_soma(matriz_entrada)
linha = pega_linha(matriz_entrada)
coluna = pega_coluna(matriz_entrada)

diagonal_verificada = verifica_igualdade_matriz(diagonal)
segunda_diagonal_verificada = verifica_igualdade_matriz(segundaDiagonal)
linha_verificada = verifica_igualdade_matriz(linha)
coluna_verificada = verifica_igualdade_matriz(coluna)

if diagonal_verificada and segunda_diagonal_verificada and linha_verificada and coluna_verificada:
    print("A Matriz é um quadrado mágico!")
else:
    print("A Matriz não é um quadrado mágico!")





