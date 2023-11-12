lista1_string = input("Informe a primeira lista: ")
lista2_string = input("Informe a segunda lista: ")

lista1_string = lista1_string.split(',')
lista_1 = []
inicio = 0
while inicio < len(lista1_string):
   lista_1.append(int(lista1_string[inicio]))
   inicio += 1

lista2_string = lista2_string.split(',')
lista_2 = []
inicio = 0
while inicio < len(lista2_string):
   lista_2.append(int(lista2_string[inicio]))
   inicio += 1

def multiplicaoLista(lista1, lista2):
   if len(lista_1) > len(lista_2):
       diferenca_tamanho = len(lista_1) - len(lista_2)
       nova_lista1 = lista_1[diferenca_tamanho:]

       cont = 0
       while cont < len(nova_lista1):
           lista_2.append(nova_lista1[cont])
           cont += 1


   elif len(lista_2) > len(lista_1):
       dife_tamanho = len(lista_2) - len(lista_1)
       nova_lista2 = lista_2[dife_tamanho:]

       cont2 = 0
       while cont2 < len(nova_lista2):
           lista_1.append(nova_lista2[cont2])
           cont2 += 1

   lista_multi = []
   cont = 0
   while cont < len(lista_1):
       resultado = lista_1[cont] * lista_2[cont]
       lista_multi.append(resultado)
       cont += 1
   return lista_multi


print(multiplicaoLista(lista_1,lista_2))
