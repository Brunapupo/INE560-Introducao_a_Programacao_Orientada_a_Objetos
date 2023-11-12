def intersecao_listas(lista1, lista2):
    return [elemento for elemento in lista1 if elemento in lista2]

# Exemplo de uso
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
print("Interseção das listas:", intersecao_listas(lista1, lista2))
