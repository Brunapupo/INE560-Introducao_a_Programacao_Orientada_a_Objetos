def maiorNumero(lista):
   maior = - 1000000
   cont = 0
   while cont < len(lista):
       if lista[cont] > maior:
           maior = lista[cont]
       cont += 1
   return maior

print(maiorNumero(lista = [10, 60, 70, 80]))
