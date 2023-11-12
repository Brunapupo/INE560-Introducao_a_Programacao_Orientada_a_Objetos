def eh_primo(numero):
   if numero == 0 or numero == 1:
       return False
   flag = False
   if numero > 1:
       for i in range(2, numero):
           if (numero % i) == 0:
               flag = True
               break
   if flag:
       return False
   else:
       return True


def primosLista(lista):
   numeros_primos = []
   for numero in lista:
       if ePrimo(numero):
           numeros_primos.append(numero)
   return numeros_primos


print(primosLista([1,3,7,9,11,15,19,60]))

