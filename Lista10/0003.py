def divisaoLista(lista):
   maior_numero = 0
   for numero in numeros_flutuantes:
       maior_numero = (max(numeros_flutuantes))
   lista_divi_numeros = []
   for numero in numeros_flutuantes:
       lista_divi_numeros.append(numero/maior_numero)
   return lista_divi_numeros


numeros = input("Informe os números: ")
numeros = numeros.split(',')
numeros_flutuantes = []

for i in numeros:
   numeros_flutuantes.append(float(i))

print(divisaoLista(numeros_flutuantes))